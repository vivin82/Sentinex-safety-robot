import rospy
from sensor_msgs.msg import LaserScan, Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

# Initialize ROS node
rospy.init_node('autonomous_robot')

# Publishers and Subscribers
cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
bridge = CvBridge()

# Movement parameters
SAFE_DISTANCE = 0.5  # Minimum safe distance from obstacles (meters)
LINEAR_SPEED = 0.2   # Forward speed
ANGULAR_SPEED = 0.5  # Angular speed

# Global variables
global_obstacle_detected = False

# Callback for LiDAR data
def lidar_callback(scan):
    global global_obstacle_detected
    
    # Process LiDAR ranges
    ranges = np.array(scan.ranges)
    min_distance = np.min(ranges[np.isfinite(ranges)])

    # Detect obstacles
    if min_distance < SAFE_DISTANCE:
        rospy.loginfo(f"Obstacle detected at {min_distance} meters.")
        global_obstacle_detected = True
    else:
        global_obstacle_detected = False

# Callback for camera data
def camera_callback(image):
    # Convert image to OpenCV format
    cv_image = bridge.imgmsg_to_cv2(image, desired_encoding='bgr8')

    # Process image (example: simple color detection)
    hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Display the processed image (optional)
    cv2.imshow('Camera View', cv_image)
    cv2.imshow('Red Object Detection', mask)
    cv2.waitKey(1)

# Main loop
if __name__ == '__main__':
    try:
        # Subscribe to LiDAR and camera topics
        rospy.Subscriber('/scan', LaserScan, lidar_callback)
        rospy.Subscriber('/camera/image_raw', Image, camera_callback)

        rate = rospy.Rate(10)  # 10 Hz

        while not rospy.is_shutdown():
            twist = Twist()

            if global_obstacle_detected:
                # Obstacle avoidance: rotate in place
                twist.linear.x = 0.0
                twist.angular.z = ANGULAR_SPEED
            else:
                # Move forward
                twist.linear.x = LINEAR_SPEED
                twist.angular.z = 0.0

            # Publish the velocity command
            cmd_vel_pub.publish(twist)
            rate.sleep()

    except rospy.ROSInterruptException:
        rospy.loginfo("Shutting down the autonomous robot node.")
    finally:
        cv2.destroyAllWindows()
