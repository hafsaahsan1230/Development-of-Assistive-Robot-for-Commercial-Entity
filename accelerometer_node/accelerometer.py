#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def callback(msg):
    ax, ay, az, gx, gy, gz = msg.data
    rospy.loginfo(f"Accel: {ax}, {ay}, {az} | Gyro: {gx}, {gy}, {gz}")

def listener():
    rospy.init_node("imu_listener", anonymous=False)
    rospy.Subscriber("imu_data", Float32MultiArray, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()
