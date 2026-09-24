import time
import cv2
from ultralytics import solutions

video_source = "vid.mp4"
cap = cv2.VideoCapture(video_source)
assert cap.isOpened(), f"Error: Could not read video file from {video_source}"

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

output_path = "parking_management_result.mp4"
video_writer = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (frame_width, frame_height)
)

parking_manager = solutions.ParkingManagement(
    model="runs/detect/train/weights/best.pt",
    json_file="bounding_boxes.json",
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    start_time = time.time()

    parking_manager(frame)

    inference_time = time.time() - start_time
    fps_value = int(1.0 / inference_time) if inference_time > 0 else 0
    cv2.putText(frame, f"FPS: {fps_value}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    video_writer.write(frame)

cap.release()
video_writer.release()
cv2.destroyAllWindows()

print(f"Video saved at '{output_path}'")

# cv2.destroyAllWindows()