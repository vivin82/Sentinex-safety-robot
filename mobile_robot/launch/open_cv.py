#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image, LaserScan
from geometry_msgs.msg import Twist
import numpy as np
import cv2
from cv_bridge import CvBridge

class LineFollower:
    def __init__(self):
        rospy.init_node('line_follower', anonymous=True)

        # Initialize the bridge to convert ROS Image messages to OpenCV format
        self.bridge = CvBridge()

        # Create a publisher to control the robot's movement
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

        # Subscribe to the camera image topic
        self.image_sub = rospy.Subscriber("/image_raw", Image, self.image_callback)

        # Subscribe to the LaserScan topic for obstacle detection
        self.scan_sub = rospy.Subscriber("/scan", LaserScan, self.scan_callback)

        self.twist = Twist()

        # PID control variables
        self.kp = 0.005  # Proportional gain
        self.ki = 0.0    # Integral gain
        self.kd = 0.001  # Derivative gain
        self.prev_error = 0
        self.integral = 0

        # # Obstacle avoidance variables
        self.obstacle_detected = False
        self.safe_distance = 0.8  # Minimum safe distance to avoid obstacles

    def detect_red_shapes(self, cv_image):
        # Convert the image to HSV color space
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        # Define the red color range in HSV
        lower_red1 = np.array([0, 120, 70])   # Lower range for red
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70]) # Upper range for red
        upper_red2 = np.array([180, 255, 255])

        # Create masks for red color
        mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
        red_mask = cv2.bitwise_or(mask1, mask2)

        # Find contours in the red mask
        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Approximate the shape
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            vertices = len(approx)
            shape = None
            if vertices == 3:
                shape = "Triangle"
            elif vertices == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                ar = w / float(h)
                shape = "Square" if 0.95 <= ar <= 1.05 else "Rectangle"
            elif vertices > 5:
                shape = "Circle"

            # Draw the detected shape and label it
            if shape:
                cv2.drawContours(cv_image, [approx], -1, (0, 255, 0), 2)
                cv2.putText(cv_image, shape, (approx[0][0][0], approx[0][0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                return shape  # Return the first detected red shape

        return None  # No red shapes detected

    def scan_callback(self, data):
        # Check if any obstacle is within the safe distance
        if any(distance < self.safe_distance for distance in data.ranges if distance > 0):
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def image_callback(self, data):
        try:
            # Convert the ROS Image message to an OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr(e)
            return

        # If an obstacle is detected, stop and avoid
        if self.obstacle_detected:
            self.avoid_obstacle()
            return

        # Detect red shapes
        detected_shape = self.detect_red_shapes(cv_image)

        if detected_shape:
            # React to detected shapes
            if detected_shape == "Triangle":
                self.twist.linear.x = 0
                self.twist.angular.z = 1.0  # Rotate in place

                # Publish the topic only for triangles
                self.cmd_vel_pub.publish(self.twist)

        else:
            # If no shapes are detected, follow the line
            self.follow_line(cv_image)

        # Display the processed image
        cv2.imshow("Line Follower with Shape Detection", cv_image)
        cv2.waitKey(3)

    # def avoid_obstacle(self):
        # Stop and rotate to avoid the obstacle
        self.twist.linear.x = 0
        self.twist.angular.z = 0.5  # Rotate to avoid
        # self.cmd_vel_pub.publish(self.twist)

    def follow_line(self, cv_image):
        # Convert to grayscale and threshold to detect the line
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY_INV)

        # Find the centroid of the line
        height, width = binary_image.shape
        moment = cv2.moments(binary_image)

        if moment['m00'] != 0:
            cx = int(moment['m10'] / moment['m00'])
            error = cx - width / 2

            # PID control
            self.integral += error
            derivative = error - self.prev_error

            control_signal = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

            self.twist.linear.x = 0.2
            self.twist.angular.z = -control_signal

            self.prev_error = error
        else:
            # Stop if no line is detected
            self.twist.linear.x = 0
            self.twist.angular.z = 0

        # self.cmd_vel_pub.publish(self.twist)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    line_follower = LineFollower()
    line_follower.run()
