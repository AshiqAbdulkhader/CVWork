from picamera import PiCamera

camera = PiCamera()
camera.vflip = True
camera.start_preview()
