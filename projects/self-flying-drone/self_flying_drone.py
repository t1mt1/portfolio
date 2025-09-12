from djitellopy import Tello
import cv2
from ultralytics import YOLO
import torch
import time


#========================#
# Import the YOLO model  #
#========================#

model = YOLO('models/yolov8s.pt')
model_path = "models/R153tello_c_FIK.pt"  


#============================#
# Initialize the Tello drone #
#============================#

tello = Tello()
tello.connect()
battery_level = tello.get_battery()
tello.streamon()
frame_read = tello.get_frame_read()

Kp_X = 0.1
Kp_Y = 0.2
Kp_Z = 0.2

# Initialize errors for PID control
integral_X = integral_Y = integral_Z = 0

desired_target_height = 300

# Takeoff and move up a bit for better visibility
tello.takeoff()
tello.move_up(30)

while True:
    img = tello.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = model(img)

    target_detected = False
    for result in results: 
        boxes = result.boxes 
        for box in boxes:
            if int(box.cls) == 39:  # Target class (bottle)
                target_detected = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Calculate center of the target box
                target_x_center = (x1 + x2) // 2
                target_y_center = (y1 + y2) // 2
                box_height = y2 - y1
                
                # PID control
                error_X = target_x_center - img.shape[1] // 2
                error_Y = img.shape[0] // 2 - target_y_center
                error_Z = desired_target_height - box_height  

                uX = Kp_X * error_X
                uY = Kp_Y * error_Y
                uZ = Kp_Z * error_Z

                print(f"Errors: {error_X}, {error_Y}, {error_Z}")
                tello.send_rc_control(int(uX), int(uZ), int(uY), 0)

                if box_height >= 300:
                    print("Landing...")
                    tello.land()
                    cv2.destroyAllWindows()


    if not target_detected:
        tello.send_rc_control(0, 5, 0, 0) # Move slowly forward if no target

    cv2.imshow("Drone Camera", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

tello.land()

cv2.destroyAllWindows()