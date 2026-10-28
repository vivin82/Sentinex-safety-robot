<<<<<<< HEAD
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DqPwyK9C)
# 221LIA001 - Robotics Lab 
## Course Project - Interim evaluation submission

All batches have to commit the following to the batch project repo;
1. **catkin_package** of the project code submitted for interim evaluation.
2. **Gazebo ROS simulation video** of the project in _webm_ format
3. List of Websites/Github/StackOverflow/ROS answers referred while realizing the interim project submission.
For item 3 main ones would do but something like https://wiki.ros.org won't do you have to mention the actual page. For instance https://wiki.ros.org/ROS/Tutorials/CreatingPackage
=======
# Sentinex

Factory safety compliance robot

Sentinex is a small four-wheel robot meant to move around a work area and check that people are wearing their safety gear. A LiDAR keeps it clear of obstacles, and a camera with a YOLO detector looks for helmets and safety vests.

The project covers the whole chain: the chassis and motor drivers, the ROS node for obstacle avoidance, and the vision model.

## How it is put together

**Base.** A four-wheel chassis with DC gear motors, run by two motor driver boards. A Raspberry Pi switches the driver inputs through eight GPIO pins, which gives forward, reverse, left, right and stop. For testing, the robot can be driven from the keyboard with w, a, s, d and x.

**Obstacle avoidance.** A ROS node listens to the LiDAR scan on `/scan`. If anything comes closer than 0.5 m, the robot stops and turns on the spot. If the way is clear, it drives forward at 0.2 m/s. Velocity commands go out on `/cmd_vel`. The same node also subscribes to the camera image on `/camera/image_raw`.

**PPE detection.** The vision work is in a Colab notebook. It downloads the Construction Site Safety image dataset from Kaggle and sets up YOLOv5 and YOLOv8 from Ultralytics, along with OpenCV code for running a model on a live webcam feed.

## Tools used

Python, ROS 1, OpenCV, NumPy, PyTorch, Ultralytics YOLO, TensorFlow/Keras, RPi.GPIO

## Running it

Motor test: run the motor control script on the Raspberry Pi and type w, a, s, d or x. Each command runs for one second and then the motors stop.

Obstacle avoidance: start `roscore`, make sure the LiDAR is publishing on `/scan` and the camera on `/camera/image_raw`, then run the ROS node.

PPE detection: open the notebook in Google Colab and run the cells in order. A GPU runtime makes training much faster.

## Where it stands

Motor control and LiDAR obstacle avoidance are written, and the notebook has the dataset and YOLO models set up. The detector is not yet connected to the drive logic. Connecting the two, so the robot stops and flags a violation when it sees someone without a helmet or vest, is the next step.

## Credits

Dataset: Construction Site Safety Image Dataset (Roboflow) by snehilsanyal on Kaggle. YOLO models by Ultralytics.

## Author

Vivin Viju, M.Tech in Robotics and Automation

## License

Copyright (c) 2026 Vivin Viju. All rights reserved. No permission is granted to use, copy, modify, or distribute this code or the design files without written permission from the author.
>>>>>>> 1cf55a51fbea5c939c01933299a8a0765820c81f
