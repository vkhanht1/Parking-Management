# Smart Parking Management System

A real-time smart parking and occupancy detection system built with Python, OpenCV, and YOLOv8, featuring an interactive Streamlit web dashboard for dynamic slot monitoring and configuration.

---

## Features

* **Real-Time YOLOv8 Detection:** Leverages Ultralytics YOLOv8 object detection models to accurately identify vehicles and monitor parking space status.
* **Interactive Web Dashboard:** Built using Streamlit to provide an intuitive user interface for video upload, system configuration, and live visual feedback.
* **Custom Slot Configuration Tool (`make_json.py`):** An interactive utility to map parking lot layouts and generate custom JSON coordinate configurations for different camera angles without hardcoding.
* **Dynamic Analytics:** Real-time calculation and display of slot occupancy metrics (Total, Stored/Occupied, and Available spaces).

---

## Project Structure

```text
ParkingManagement/
├── app.py                     # Streamlit web interface dashboard
├── make_json.py               # Interactive parking slot selection and JSON generator
├── main.py                    # Core OpenCV and YOLOv8 video processing script
├── slot_specification.py      # Helper module for coordinate and slot handling
├── download_data.py           # Dataset acquisition script
├── bounding_boxes.json        # Default JSON configuration file for parking slots
├── reference_image.jpg        # Reference image for layout calibration
├── vid.mp4                    # Sample test video stream
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

```

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone (https://github.com/vkhanht1/Parking-Management.git)
cd ParkingManagement

```


2. **Install dependencies:**
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt

```


3. **Run the Streamlit Web Application:**
```bash
streamlit run app.py

```



---

## Usage Guide

1. Open the Streamlit dashboard in your web browser (usually `http://localhost:8501`).
2. Use the **Configuration Panel** on the sidebar to specify your model weights path and JSON slot configuration file.
3. Upload an MP4 parking video file.
4. View the real-time detection results, bounding boxes, and dynamic occupancy counts directly on the dashboard.
