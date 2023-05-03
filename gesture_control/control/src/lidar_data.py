#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from control.msg import LidarData


def callback(data):
    pub = rospy.Publisher('/lidar_data', LidarData, queue_size = 10)  # publisher for Lidar readings (LidarData)
    lidar = LidarData()
    lidar.dist_f = data.ranges[0]                                     # front lidar data
    lidar.dist_b = data.ranges[len(data.ranges) // 2]                 # back lidar data
    rospy.loginfo("Front: {:.3f}, Back: {:.3f}".format(lidar.dist_f, lidar.dist_b))
    pub.publish(lidar)


def read_lidar():
    rospy.init_node('lidar', anonymous=True)        # initialize node
    rospy.Subscriber('/scan', LaserScan, callback)  # subscriber for all Lidar information (LaserScan)
    rospy.spin()


if __name__ == '__main__':
    try:
        read_lidar()
    except rospy.ROSInterruptException:
        pass
