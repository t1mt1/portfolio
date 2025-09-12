# Self-Driving Drone with Computer Vision  

This project implements a simple autonomous drone navigation system using a **DJI Tello** drone and a **YOLOv8 object detection model**. The drone detects a target object in its camera feed, flies toward it using proportional control (PID-like), and lands once the target is reached.  

---

## Features  
- **Real-time object detection** using YOLOv8  
- **Autonomous navigation** toward a chosen target (a bottle)  
- **PID-inspired control** of drone movement (based on errors in X, Y, Z)  

---

## How It Works  
1. Connect to the DJI Tello and start the camera stream.  
2. Run YOLOv8 on each video frame to detect objects.  
3. If the target object is detected:  
   - Calculate the target’s center and bounding box height  
   - Compute position errors relative to the image center  
   - Send control commands to move the drone closer  
4. When the target fills a sufficient part of the frame (box height ≥ threshold), land  

If no target is detected, the drone maintains a hovering/slow forward motion.  

---

## Requirements  
- Python 3.9+  
- [djitellopy](https://github.com/damiafuentes/DJITelloPy)  
- [ultralytics](https://github.com/ultralytics/ultralytics) (YOLOv8)  
- OpenCV  
- PyTorch  

Install dependencies:  
```bash
pip install djitellopy ultralytics opencv-python torch
```

Run the navigation script:
```bash
python drone_navigation.py
```
The drone will take off, search for the target, and navigate toward it.
