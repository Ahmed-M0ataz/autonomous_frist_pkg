#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class RobotController:
    def __init__(self):
        rospy.init_node('robot_controller')
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.cmd = Twist()
        self.obstacle_detected = False
        self.obstacle_detected_right = False

    def laser_callback(self, data):
        # Check if an obstacle is within 1 meter
        min_range_forward = min(data.ranges[300:400])
        if min_range_forward < 1.0:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False
        min_range_right = min(data.ranges[0:100])
        if min_range_right < 1.0:
            self.obstacle_detected_right = True
        else:
            self.obstacle_detected_right = False
    def navigate_obstacle(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            if not self.obstacle_detected:
            #    move forward
                self.cmd.linear.x = 0.8  # Adjust the linear velocity as needed
                self.cmd.angular.z = 0.0  
                if not self.obstacle_detected_right:
                    self.cmd.linear.x = 0.0  # Adjust the linear velocity as needed
                    self.cmd.angular.z = 0.5 
                    
            else:
                # Obstacle detected, navigate around it
                self.cmd.linear.x = 0.0  # Stop linear movement
                self.cmd.angular.z = 0.6  # Rotate left (adjust as needed)

            self.cmd_pub.publish(self.cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        controller = RobotController()
        controller.navigate_obstacle()
    except rospy.ROSInterruptException:
        pass