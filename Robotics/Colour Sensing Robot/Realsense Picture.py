
import pyrealsense2 as rs
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from time import sleep


def take_picture(msg: String):
    rospy.loginfo("Confirmation recieved.")

    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()

    # Get device product line for setting a supporting resolution
    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)
    device = pipeline_profile.get_device()

    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # Start streaming
    pipeline.start(config)

    try:
        while True:
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue

            # Convert images to numpy arrays
            color_image = np.asanyarray(color_frame.get_data())

            #print(color_image)

            msg_frame = CvBridge().cv2_to_imgmsg(color_image)
            pub.publish(msg_frame)
            rospy.loginfo("Picture Taken.")
            break

    finally:

        # Stop streaming
        pipeline.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":

    rospy.init_node("Camera")

    pub = rospy.Publisher("Images", Image, queue_size=1)
    sub = rospy.Subscriber("/Confirm", String, callback=take_picture)

    rospy.loginfo("Started Camera.")

    rospy.spin()