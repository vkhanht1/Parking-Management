from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data="Car-Detection-1/data.yaml",
    epochs=50,
    imgsz=640,
    device="cpu"
)