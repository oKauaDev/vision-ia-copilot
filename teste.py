import cv2
import numpy as np
import argparse

def load_model():
    net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')
    return net

def detect_objects(frame, net):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    return detections

def main(args):
    net = load_model()

    cap = cv2.VideoCapture(args.camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    cap.set(cv2.CAP_PROP_FPS, args.fps)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect_objects(frame, net)

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > args.score_threshold:
                class_id = int(detections[0, 0, i, 1])
                class_name = classNames[class_id]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                label = "{}: {:.2f}%".format(class_name, confidence * 100)
                cv2.putText(frame, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Object Detection with OpenCV')
    parser.add_argument('-camera', type=int, help='Camera index', default=0)
    parser.add_argument('-fps', type=int, help='Frames per second', default=60)
    parser.add_argument('-width', type=int, help='Frame width', default=1280)
    parser.add_argument('-height', type=int, help='Frame height', default=720)
    parser.add_argument('-score_threshold', type=float, help='Confidence score threshold', default=0.2)

    args = parser.parse_args()

    classNames = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
                  "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa",
                  "train", "tvmonitor"]

    main(args)
