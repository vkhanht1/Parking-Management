import cv2
from ultralytics import solutions

cap = cv2.VideoCapture("vid.mp4")
ret, frame = cap.read()
cap.release()

if ret:
    cv2.imwrite("reference_image.jpg", frame)
    print("Created reference_image.jpg successful.")

solutions.ParkingPtsSelection()