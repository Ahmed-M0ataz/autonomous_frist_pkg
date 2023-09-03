#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class MoveCar:
    def __init__(self):
        self.pub_msg = Twist()
        self.yaw_degrees = 0.0
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # use adom to know what angle the car is in and use laser to know the distance
        self.sub_angle = rospy.Subscriber("/odom", Odometry, self.odometry_callback)
        self.sub_laser = rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        self.rate = rospy.Rate(5)  # 10Hz
               
    def odometry_callback(self, msg):
        
        # Extract orientation (quaternion) from odometry message
        orientation = msg.pose.pose.orientation
        # Convert quaternion to Euler angles (roll, pitch, yaw)
        roll, pitch, yaw = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        # Convert yaw to degrees
        self.yaw_degrees = yaw * 180.0 / 3.14159265359
    
    def laser_callback(self, msg):
        rospy.loginfo('the angle is in z axis %f', self.yaw_degrees)
        print(f'the destance forward is : {msg.ranges[360]}')
        # get min range in directions
        min_range_forward = min(msg.ranges[350:470])
        min_range_right = min(msg.ranges[0:20])
        min_range_left = min(msg.ranges[700:719])
        
        self.pub_msg.linear.x = 0.8
        self.pub_msg.angular.z = 0
        self.pub.publish(self.pub_msg)
        
        if (msg.ranges[360] > 1) :
                rospy.loginfo('in direction Forward')                   
                self.pub_msg.linear.x = 0.8
                self.pub_msg.angular.z = 0
                self.pub.publish(self.pub_msg)

        else:   
            self.pub_msg.linear.x = 0.0
            self.pub_msg.angular.z = 0
            self.pub.publish(self.pub_msg)    
            if min_range_forward < 1 or min_range_right < 1:
                rospy.loginfo('left')
                self.pub_msg.linear.x = 0
                self.pub_msg.angular.z = 0.5
                self.pub.publish(self.pub_msg)
                rospy.loginfo('range in left is %f',msg.ranges[0])
                rospy.loginfo('range in right is %f',msg.ranges[719])
                
                ## that use to rotate the robot by 90 degree but it is not working now 
                # while self.yaw_degrees < 90:
                #     rospy.loginfo('still left')
                #     self.pub_msg.linear.x = 0
                #     self.pub_msg.angular.z = 0.5
                #     self.pub.publish(self.pub_msg)
                #     rospy.loginfo('range in left is %f',msg.ranges[0])
                #     rospy.loginfo('range in right is %f',msg.ranges[719])
        
            elif min_range_left < 1:
                rospy.loginfo('right')
                self.pub_msg.linear.x = 0
                self.pub_msg.angular.z = -0.5
                self.pub.publish(self.pub_msg)
            
if __name__ == '__main__':
    rospy.init_node('move_car')
    move_car = MoveCar()
    rospy.spin()
