#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

cmd = "Stop"


def callback(data):
    global cmd
    rospy.loginfo(f"Command: {data.data}")
    cmd = data.data


def command():
    rospy.init_node('command', anonymous=True)               # initialize node
    rospy.Subscriber('/gesture', String, callback)           # subscriber for gesture command (String)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # publisher for linear/angular command velocity (Twist)
    rate = rospy.Rate(10)                                    # 10Hz rate
    while not rospy.is_shutdown():
        twist = Twist()
        if cmd == "Move Forward":
            twist.linear.x = 0.5; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        elif cmd == "Move Backward":
            twist.linear.x = -0.5; twist.linear.y = 0.0; twist.linear.z = 0.0
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
