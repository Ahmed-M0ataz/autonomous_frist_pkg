#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

# Import statements for TF
from tf import TransformListener
from tf.transformations import euler_from_quaternion
import tf
flag = 0
class MoveCar:
    def __init__(self):
        self.pub_msg = Twist()
        self.listener = TransformListener()
        self.laser_msg = LaserScan()
        self.yaw_degrees = 0.0
        # self.flag = 0
        self.flag_right = 0
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub_angle = rospy.Subscriber("/odom", Odometry, self.odometry_callback)
        self.sub_laser = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        # self.sub_angle = rospy.Subscriber("/tf", tf.msg.tfMessage, self.tf_callback)

        self.rate = rospy.Rate(5)  # 10Hz

        # while not rospy.is_shutdown():
               
    def odometry_callback(self, msg):
        
        # Extract orientation (quaternion) from odometry message
        orientation = msg.pose.pose.orientation
        # Convert quaternion to Euler angles (roll, pitch, yaw)
        roll, pitch, yaw = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        # Convert yaw to degrees
        self.yaw_degrees = yaw * 180.0 / 3.14159265359
    
    def tf_callback(self,msg):
    
        # Get the orientation of the robot base link
        (trans, rot) = self.listener.lookupTransform("/base_link", "/hokuyo_link", rospy.Time(0))
        
        # Convert quaternion to Euler angles (roll, pitch, yaw)
        roll, pitch, yaw = tf.transformations.euler_from_quaternion(rot)
        
        # Convert yaw to degrees
        self.yaw_degrees = yaw * 180.0 / 3.14159265359
    def laser_callback(self, msg):
        self.laser_msg = msg
        rospy.loginfo('the angle is in z axis %f', self.yaw_degrees)
        print(f'the destance forward is : {msg.ranges[360]}')
       
     
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
        #         flag = 1
        #         self.flag_right = 1
        #         rospy.loginfo('range in forward is %f',msg.ranges[360])
        #         rospy.loginfo('range in right is %f',msg.ranges[719])
        #         rospy.loginfo('range in left is %f',msg.ranges[0])
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
                # while self.yaw_degrees < 90:
                #     rospy.loginfo('still left')
                #     self.pub_msg.linear.x = 0
                #     self.pub_msg.angular.z = 0.5
                #     self.pub.publish(self.pub_msg)
                #     rospy.loginfo('range in left is %f',msg.ranges[0])
                #     rospy.loginfo('range in right is %f',msg.ranges[719])
            
            
            # if  :
            #     rospy.loginfo('left')
            #     self.pub_msg.linear.x = 0
            #     self.pub_msg.angular.z = 0.5
            #     self.pub.publish(self.pub_msg)
                
            elif min_range_left < 1:
                rospy.loginfo('right')
                self.pub_msg.linear.x = 0
                self.pub_msg.angular.z = -0.5
                self.pub.publish(self.pub_msg)
            # while self.yaw_degrees > 0:
            #     rospy.loginfo('still right')
            #     rospy.loginfo('range in left is %f',msg.ranges[0])
            #     rospy.loginfo('range in right is %f',msg.ranges[719])
            #     self.pub_msg.linear.x = 0
            #     self.pub_msg.angular.z = -0.5
            #     self.pub.publish(self.pub_msg) 
            # flag = 0 
        
            # while  msg.ranges[0] < 2:
            #     rospy.loginfo('go to forward')
            #     rospy.loginfo('data is %f', msg.ranges[0])
            #     rospy.loginfo('data is %f', msg.ranges[719])
                
            #     print('type is :')
            #     print(type(msg.ranges[0]))
            #     print('type last is  :')
            #     print(type(msg.ranges[719]))
            #     self.pub_msg.linear.x = 0.5
            #     self.pub_msg.angular.z = 0.0
            #     self.pub.publish(self.pub_msg)
            #     rospy.sleep(0.1)
            #     if msg.ranges[0] >= 1.735273:
            #         break
            #     if msg.ranges[0] == float('inf'):
            #         break
        
                
            # # if msg.ranges[720] > 1:    
            # rospy.loginfo('right')
            # self.pub_msg.linear.x = 0
            # self.pub_msg.angular.z = -0.5
            # self.pub.publish(self.pub_msg)
                
            # while self.yaw_degrees > 0:
            #     rospy.loginfo('still right')
            #     self.pub_msg.linear.x = 0
            #     self.pub_msg.angular.z = -0.5
            #     self.pub.publish(self.pub_msg)  
            # self.pub_msg.linear.x = 0.5
            # self.pub_msg.angular.z = 0.0
            # self.pub.publish(self.pub_msg)  
                 
        # else :
        #     rospy.loginfo('Forward')    
        #     rospy.loginfo('range in left is %f',msg.ranges[0])
        #     rospy.loginfo('range in right is %f',msg.ranges[719])               
        #     self.pub_msg.linear.x = 0.5
        #     self.pub_msg.angular.z = 0
        #     self.pub.publish(self.pub_msg)
if __name__ == '__main__':
    rospy.init_node('move_car')
    move_car = MoveCar()
    rospy.spin()
