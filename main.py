import numpy as np
import keyboard
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from utils.Cache import Cache
from utils.Distance import calcDirection
from helpers.Voice import Voice
from helpers.Humanization import humanize
from helpers.DataInfos import get_object_infos
from debug.Window import Window

MODEL_PATH = 'models/efficientdet.tflite'

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.6)
detector = vision.ObjectDetector.create_from_options(options)

cap = cv2.VideoCapture(0)
voice = Voice()
cache = Cache()
window = Window("Vision Copilot")

def executeObject(image, detections, camWidth):
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
      if real_object:
        classname = real_object["name"]
      
      window.drawInObject(image, x, y, width, height, classname)
      if cache.get(classname) is None:
        next_cache = cache.get("NEXT_{}".format(classname.upper()))
        if next_cache is None or next_cache <= 3:
          if next_cache is None:
            cache.set("NEXT_{}".format(classname.upper()), 1, 6)
          else:
            cache.set("NEXT_{}".format(classname.upper()), next_cache + 1, 6)
        else:
          direction = calcDirection(camWidth, x, width)
          objects.append((classname, direction, real_object["gender"]))
          cache.set(classname, True, 15)
  
  if objects:
    def onEnd():
      print("Fala acabou")
    
    speeker = humanize(objects)
    voice.speak(speeker, onEnd)


while cap.isOpened:
    success, image = cap.read()
    if success:
      height, width, _ = image.shape
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image.flags.writeable = False
      
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
      detection_result = detector.detect(mp_image)
      
      if detection_result.detections:
        executeObject(image, detection_result.detections, width)

      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image.flags.writeable = True
      window.shot(image)
    
    if keyboard.is_pressed('q'):
      break

cap.release()
window.destroy()
    