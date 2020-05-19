import cv2
import time
import pyfakewebcam

cap = cv2.VideoCapture('http://localhost:1224/video')

camera = pyfakewebcam.FakeWebcam('/dev/video1', 1024, 768)

while True:
    ret, frame = cap.read()
    camera.schedule_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #time.sleep(1 / 30.0)