#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int32MultiArray

def comm():
    pub = rospy.Publisher('comm', Int32MultiArray, queue_size=10)
    rospy.init_node('comm', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    hello_str = Int32MultiArray()
    hello_str.data = [2, 1, 2]
    while not rospy.is_shutdown():
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        comm()
    except rospy.ROSInterruptException:
        pass
