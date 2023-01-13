#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
pub = ""

def callback(data):
    if("turtle" in data.data and "dance" in data.data):
        print('dancing')
        move_cmd = Twist()
        move_cmd.angular.z = 2.0
        pub.publish(move_cmd)
        time.sleep(10)
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)
        

def dance():
    global pub
    rospy.init_node('dance')

    rospy.Subscriber('/speech_recognition/final_result', String, callback)
    rospy.Subscriber('/dancer', String, callback)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    rospy.spin()

if __name__ == '__main__':
    dance()