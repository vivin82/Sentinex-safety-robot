# Robotics & Automation Portfolio
**Author:** Vivin Viju | M.Tech in Robotics and Automation

Welcome to my engineering portfolio. This single repository contains the source code, ROS workspaces, hardware schematics, and simulation files for my work in robotics, embedded systems, computer vision, and mechanical design.

---

## 🚀 Featured Project: Sentinex (Factory Safety Compliance Robot)
*Directory: `/sentinex`*

Sentinex is a 4WD autonomous mobile robot designed to monitor industrial workspaces and ensure personnel are complying with safety gear protocols. By fusing LiDAR-based spatial awareness with a YOLO-driven computer vision pipeline, the rover navigates active environments to detect the presence of hardhats and high-visibility safety vests.

### Hardware & Kinematics
* **Base Chassis:** A custom four-wheel drive chassis utilizing DC gear motors, controlled by two independent motor driver boards.
* **Core Compute:** A Raspberry Pi handles the high-level logic, switching the motor driver inputs via 8 GPIO pins to execute Forward, Reverse, Left, Right, and Stop commands.
* **Sensors:** 2D LiDAR for environmental scanning and a standard camera for real-time visual feeds.

### Software & Perception
* **Obstacle Avoidance (ROS 1):** A dedicated ROS node subscribes to the `/scan` topic. If the path is clear, the robot maintains a forward velocity of 0.2 m/s via `/cmd_vel`. If an obstacle is detected within 0.5m, the robot halts and executes an in-place rotation. 
* **PPE Detection Pipeline:** The vision model is currently staged in a Google Colab notebook. It leverages OpenCV to run YOLOv5 and YOLOv8 models to detect safety helmets and vests on a live video feed.

### How to Run Sentinex
1. **Motor Control:** Run the standalone Python script on the Raspberry Pi and use `W`, `A`, `S`, `D`, `X` to drive manually.
2. **ROS Navigation:** Run `roscore`, ensure LiDAR is publishing to `/scan`, and run the `obstacle_avoidance.py` node.
3. **Vision Pipeline:** Open the Colab notebook, select a GPU runtime, and execute cells sequentially.

*Status: Motor control, LiDAR avoidance, and standalone YOLO detection are complete. Currently integrating the perception pipeline directly with the drive logic to enable autonomous violation flagging.*

---

## 📂 Additional Portfolio Projects

*Note: Documentation and source code for the following systems are organized in their respective folders within this repository.*

### 1. Autonomous Outdoor Surveillance Rover
A 4WD mobile robot designed for outdoor surveillance using ROS, Teach-and-Repeat navigation, YOLOv8 human vision detection, and an NVIDIA Jetson TX2.

### 2. Elderly Assistance Mobile Robot
A multi-functional assistive robot integrating smartwatch BLE RSSI tracking, ultrasonic sensor fusion, and heart rate monitoring using a dual-microcontroller architecture (Arduino UNO R4 & ESP32).

### 3. 6-DOF PUMA Robotic Arm Kinematics
Kinematics simulation and trajectory planning for a 6-DOF robotic manipulator, validated using ROS and Gazebo.

### 4. Thermal-to-RGB Image Colorization
A deep learning computer vision model trained to convert thermal and infrared images into the visible spectrum.

### 5. Automated Pre-Impact Bumper System
Mechanical design and fabrication of a vehicle bumper system designed to automatically extend and absorb collision forces prior to impact.

---

## 🛠️ Technical Stack
* **Frameworks & Middleware:** ROS 1, Gazebo, Webots, OpenCV, YOLO (v5/v8), PyTorch, TensorFlow/Keras.
* **Languages:** Python, C++, C.
* **Hardware Platforms:** NVIDIA Jetson TX2, Raspberry Pi, Arduino UNO R4, ESP32, RPLIDAR.

---

## 📝 Credits & License
* **Sentinex Dataset:** Construction Site Safety Image Dataset (Roboflow) by snehilsanyal on Kaggle.
* **Sentinex Models:** Ultralytics YOLO.
* **License:** Copyright (c) 2026 Vivin Viju. All rights reserved. No permission is granted to use, copy, modify, or distribute this code or the design files without written permission from the author.
