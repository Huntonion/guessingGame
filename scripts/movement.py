#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    if('link' in data.data and'come' in data.data):
        print('okay i\'ll come there')

def movement():

    rospy.init_node('movement')

    rospy.Subscriber('/speech_recognition/final_result', String, callback)

    rospy.spin()

if __name__ == '__main__':
    movement()