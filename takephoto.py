import time
from picamera import PiCamera
camera = PiCamera()
camera.start_preview()
time.sleep(2)
camera.capture('./fot.jpg',resize=(100,100))
time.sleep(2)
camera.capture('./raopi.jpg',resize=(100,100))