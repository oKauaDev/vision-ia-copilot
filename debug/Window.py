import cv2

class Window:
  name = ""
  
  def __init__(self, name):
    self.name = name
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
  
  def shot(self, image):
      cv2.imshow(self.name, image)
  
  def drawInObject(self, image, x, y, width, height, classname):
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    cv2.putText(image, classname, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
  
  def destroy():
    cv2.destroyAllWindows()
    