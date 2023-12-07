print("Iniciando carregamento...")

import argparse
import numpy as np
import keyboard
import mediapipe as mp
from mediapipe.python import solutions as mp_solutions
import cv2
from utils.Cache import Cache
from utils.Distance import calcDirection, calcPositionX
# from helpers.Voice import Voice
from helpers.Humanization import humanize
from helpers.DataInfos import get_object_infos
from debug.Window import Window

def main(args):
    print("""
    #     #                              #####                                      
    #     # #  ####  #  ####  #    #    #     #  ####  #####  # #       ####  ##### 
    #     # # #      # #    # ##   #    #       #    # #    # # #      #    #   #   
    #     # #  ####  # #    # # #  #    #       #    # #    # # #      #    #   #   
      #   #  #      # # #    # #  # #    #       #    # #####  # #      #    #   #   
    # #   # #    # # # #    # #   ##    #     # #    # #      # #      #    #   #   
      #    #  ####  #  ####  #    #     #####   ####  #      # ######  ####    #   
                                                                                  
        """)

    MODEL_PATH = 'models/efficientdet.tflite'

    print("score_threshold: {}".format(args.score_threshold))
    print("max_results: {}".format(args.max_results))
    print("width: {}".format(args.width))
    print("height: {}".format(args.height))
    print("fps: {}".format(args.fps))
    print("")

    print("Carregando modelo...")
    base_options = mp_solutions.BaseOptions(model_asset_path=MODEL_PATH)
    options = mp_solutions.object_detection.ObjectDetectorOptions(
        base_options=base_options,
        score_threshold=args.score_threshold,
        max_results=args.max_results
    )
    detector = mp_solutions.object_detection.ObjectDetector(options=options)

    print("Criando classes")
    cap = cv2.VideoCapture(args.camera)
    # voice = Voice()
    cache = Cache()
    window = Window("Vision Copilot")

    print("Definindo configurações da câmera...")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    cap.set(cv2.CAP_PROP_FPS, args.fps)

    def executeObject(image, detections, camWidth, camHeight):
        objects = []

        for detection in detections:
            classnames = detection.categories

            bbox = detection.bounding_box
            x = int(bbox.origin_x)
            y = int(bbox.origin_y)
            width = int(bbox.width)
            height = int(bbox.height)

            for category in classnames:
                classname = category.category_name
                real_object = get_object_infos(classname)
                directionX = calcPositionX(camWidth, x, width)
                gender = ""
                if real_object:
                    classname = real_object["name"]
                    gender = real_object["gender"]

                window.drawInObject(image, x, y, width, height, classname)
                if cache.get("{}{}".format(classname, directionX)) is None:
                    next_cache = cache.get("NEXT_{}".format(classname.upper()))
                    if next_cache is None or next_cache <= 3:
                        if next_cache is None:
                            cache.set("NEXT_{}".format(classname.upper()), 1, 6)
                        else:
                            cache.set("NEXT_{}".format(classname.upper()), next_cache + 1, 6)
                    else:
                        direction = calcDirection(camWidth, camHeight, x, y, width, height)
                        objects.append((classname, direction, gender))
                        cache.set("{}{}".format(classname, directionX), True, 15)

        if objects:
            speaker = humanize(objects)
            # voice.speak(speaker)

    print("Vision Copilot iniciado")
    # voice.speak("Vision Copilot iniciado.")
    while cap.isOpened:
        success, image = cap.read()
        if success:
            height, width, _ = image.shape
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
            detection_result = detector.detect(mp_image)

            if detection_result.detections:
                executeObject(image, detection_result.detections, width, height)

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = True
            window.shot(image)

        if keyboard.is_pressed('q'):
            break

    cap.release()
    window.destroy()
    # voice.speak("Vision Copilot desligado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Vision Copilot - Sistema de Detecção de Objetos.')
    parser.add_argument('-camera', type=int, help='Ativar a câmera', default=0)
    parser.add_argument('-fps', type=int, help='Pegar o fps', default=60)
    parser.add_argument('-width', type=int, help='Width da câmera', default=1280)
    parser.add_argument('-height', type=int, help='Height da câmera', default=720)
    parser.add_argument('-score_threshold', type=float, help='Height da câmera', default=0.55)
    parser.add_argument('-max_results', type=int, help='Height da câmera', default=3)

    args = parser.parse_args()

    main(args)