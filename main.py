import cv2
import time
import pyfakewebcam

cap = cv2.VideoCapture('http://127.0.0.1:1224/video')

# Note - you have to manually set the dimensions here, according
# to the settings in the ip webcam app
camera = pyfakewebcam.FakeWebcam('/dev/video1', 1280, 720)

while True:
    ret, frame = cap.read()
    try:
        camera.schedule_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    except Exception as e:
        print(e)
