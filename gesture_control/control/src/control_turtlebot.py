#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from control.msg import LidarData

cmd = "Stop"
dist_f = 0
dist_b = 0


def callback1(data):
    global cmd
    cmd = data.data


def callback2(data):
    global dist_f, dist_b
    dist_f, dist_b = data.dist_f, data.dist_b


def command():
    rospy.init_node('command', anonymous=True)               # initialize node
    rospy.Subscriber('/gesture', String, callback1)          # subscriber for gesture command (String)
    rospy.Subscriber('/lidar_data', LidarData, callback2)    # subscriber for Lidar readings (LidarData)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # publisher for linear/angular command velocity (Twist)
    rate = rospy.Rate(10)                                    # 10Hz rate
    while not rospy.is_shutdown():
        twist = Twist()
        if (cmd == "Move Forward" and dist_f <= 0.3) or (cmd == "Move Backward" and dist_b <= 0.3):
            twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        elif cmd == "Move Forward" and dist_f > 0.3:
            twist.linear.x = 0.2; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        elif cmd == "Move Backward" and dist_b > 0.3:
            twist.linear.x = -0.2; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        elif cmd == "Turn Left":
            twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 1.0
        elif cmd == "Turn Right":
            twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = -1.0
        else:
            twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        
        pub.publish(twist)
        rate.sleep()


if __name__ == '__main__':
    try:
        command()
    except rospy.ROSInterruptException:
        pass
