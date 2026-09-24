from roboflow import Roboflow

rf = Roboflow(api_key="3mndcWfojrGN5DfsLj5z")
project = rf.workspace("van-khanh-tran").project("car-detection-kz4wd")
dataset = project.version(1).download("yolov8")

print("Download successful at:", dataset.location)