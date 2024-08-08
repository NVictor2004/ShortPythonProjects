#!/usr/bin/env python3

from re import L
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
from martypy import Marty
from time import sleep

def robot_callback(msg: Image):
    rospy.loginfo("Picture Recieved.")
    image = CvBridge().imgmsg_to_cv2(msg)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    height, width, _ = image.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_centre = hsv_image[cy, cx]
    hue = pixel_centre[0]

    #print(hue)

    if 0 <= hue < 20 or 170 < hue <= 180:
        color = "RED"
        robot.dance()
    elif 20 <= hue < 40:
        color = "YELLOW"
        robot.walk(2, "auto", 0, -10, 1000)
    elif 40 <= hue < 80:
        color = "GREEN"
        robot.walk(2, "auto", 0, 10, 1000)
    elif 80 <= hue < 120:
        color = "BLUE"
        robot.sidestep("left", 2, 25, 1000)
    elif 120 <= hue <= 170:
        color = "PURPLE"
        robot.sidestep("right", 2, 25, 1000)
    
    pub.publish("Confirmation")
    rospy.loginfo("Confirmation Sent")
    print(color)

if __name__ == "__main__":
    rospy.init_node("Robot")

    robot = Marty("wifi", "10.42.0.67")

    sub = rospy.Subscriber("/Images", Image, callback=robot_callback)
    pub = rospy.Publisher("Confirm", String, queue_size = 1)

    rospy.loginfo("Started Robot")
    sleep(5)
    pub.publish("Confirmation")

    rospy.spin()

    