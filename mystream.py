from picamera import PiCamera 
from io import BytesIO
from time import sleep
import cv2
my_stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(my_stream,'jpeg')
data = my_stream.array
cv2.imshow("12",data)