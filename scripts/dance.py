#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def startDancing(data):
    print(data.data)

def callback(data):
    if("link" in data.data and "dance" in data.data):
        print("okay, i will dance!!")

def dance():

    rospy.init_node('dance')

    rospy.Subscriber('/speech_recognition/final_result', String, callback)
    rospy.Subscriber('/dancer', String, startDancing)
    

    rospy.spin()

if __name__ == '__main__':
    dance()