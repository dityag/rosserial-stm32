#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    talker()
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('com', anonymous=True)

    rospy.Subscriber("stmPub", Int32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def talker():
    comPub = rospy.Publisher('comPub', Int32MultiArray, queue_size=10)
    rospy.init_node('com', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    a = Int32MultiArray()
    a.data = [100, 200]
    while not rospy.is_shutdown():
        rospy.loginfo(a)
        comPub.publish(a)
        rate.sleep()

if __name__ == '__main__':
    talker()
    listener()
