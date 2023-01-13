#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

pub = ""
move_cmd = ""

def stop():
    move_cmd= Twist()
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

def callback(data):
    global move_cmd
    move_cmd = Twist()

    if('turtle' in data.data and'forward' in data.data):
        stop()
        move_cmd.linear.x = 0.2
        pub.publish(move_cmd)
    if('turtle' in data.data and'left' in data.data):
        stop()
        move_cmd.angular.z = 0.5
        pub.publish(move_cmd)
    if('turtle' in data.data and'right' in data.data):
        stop()
        move_cmd.angular.z = -0.5
        pub.publish(move_cmd)
    if('turtle' in data.data and'stop' in data.data):
        stop()


def movement():
    global pub
    rospy.init_node('movement')

    rospy.Subscriber('/speech_recognition/final_result', String, callback)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    rospy.spin()

if __name__ == '__main__':
    movement()