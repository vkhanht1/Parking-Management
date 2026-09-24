import cv2
import os

# 1. Create a folder to store your training images
output_dir = "dataset_images"
os.makedirs(output_dir, exist_ok=True)

# 2. Open the video file
video_source = "vid.mp4"
cap = cv2.VideoCapture(video_source)
assert cap.isOpened(), f"Error: Could not open {video_source}"

# 3. Get FPS to extract roughly 1 frame per second
fps = int(cap.get(5))  # CV_CAP_PROP_FPS
frame_count = 0
saved_count = 0

print("Starting to extract frames for training...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Save 1 frame every second (e.g., every 30th frame if video is 30fps)
    if frame_count % fps == 0:
        image_name = os.path.join(output_dir, f"frame_{saved_count:03d}.jpg")
        cv2.imwrite(image_name, frame)
        saved_count += 1

        # We only need about 40 images for a quick fine-tune
        if saved_count >= 40:
            break

    frame_count += 1

cap.release()
print(f"Extraction complete! Saved {saved_count} images to the '{output_dir}' folder.")