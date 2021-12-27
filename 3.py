import time
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1500,1900)
camera.start_preview()
time.sleep(2)
camera.capture('./fot.jpg')
