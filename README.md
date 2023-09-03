# autonomous_frist_pkg

### Purpose of this Package

This package serves the following purposes:

1. Create a `URDF` (Unified Robot Description Format) file for a differential robot.
2. Set up a Gazebo environment.
3. Add all Gazebo package requirements for differential drive, lidar, or depth camera.
4. Create Python scripts to enable basic autonomous robot movement.

## Prerequisites

Before you start working with this package, ensure you have the following prerequisites:

1. A functional ROS workspace. If you don't have one, you can create a workspace by following the [official ROS tutorial on creating a package](http://wiki.ros.org/ROS/Tutorials/CreatingPackage).

## Steps to Create this package

Follow these steps to create a URDF file for your differential robot:

1. **Create a ROS Package**

   If you haven't already set up a ROS workspace and package, you can create one by referring to the official ROS tutorial mentioned in the prerequisites.

2. **Create a URDF File**

   Inside your ROS package directory, create a folder named `urdf`. This folder will be used to store your URDF files, create a new file with the extension `.xacro`. You can choose any name for this file, but for this example, let's name it `file.xacro`. You can write your robot's URDF description in this file by following the guidelines provided in the [official ROS URDF tutorial](http://wiki.ros.org/urdf/Tutorials).

3. **Create a Gazebo enviroment File**

    folow this tutorial :
    [official Building a world](http://classic.gazebosim.org/tutorials?tut=build_world&cat=build_world).

4. **Create a Lauch File**
    folow this tutorial :
    [official Building a world](hhttp://classic.gazebosim.org/tutorials?tut=ros_roslaunch).

## Robot Autonomous Control

To control your robot's movement autonomously, you can use a Publisher to write to the `/cmd_vel` topic and a Subscriber to read from the `/kobuki/laser/scan` topic. Here's a compact explanation of the control logic:

1. **Publisher for `/cmd_vel` Topic:**

   Create a Publisher that writes into the `/cmd_vel` topic to move the robot. You will adjust the linear and angular velocity values based on the laser sensor readings.

2. **Subscriber for `/kobuki/laser/scan` Topic:**

   Create a Subscriber that reads data from the `/kobuki/laser/scan` topic. This topic contains laser sensor data, which you will use to make decisions about robot movement.

3. **Control Logic:**

   - If the laser reading in front of the robot is higher than 1 meter (indicating no obstacle within 1 meter in front), set the robot to move forward.
   
   - If the laser reading in front of the robot is lower than 1 meter (indicating an obstacle closer than 1 meter in front), make the robot turn left.
   
   - If the laser reading at the right side of the robot is lower than 1 meter (indicating an obstacle closer than 1 meter on the right side), make the robot turn left.
   
   - If the laser reading at the left side of the robot is lower than 1 meter (indicating an obstacle closer than 1 meter on the left side), make the robot turn right.

This logic ensures that the robot can navigate autonomously based on its laser sensor readings, avoiding obstacles in its path.

Implement this control logic in your ROS nodes to achieve autonomous robot movement.

## Starting the Package

Follow these steps to start the `autonomous_frist_pkg` package:

1. **Launch `robot.launch`:**

   To launch the `robot.launch` file, use the following command:

   ```shell
   roslaunch autonomous_frist_pkg robot.launch
1. **Launch `robot_move.launch`:**

   To launch the `robot_move.launch` file, use the following command:

   ```shell
   roslaunch autonomous_frist_pkg robot_move.launch

## Output is 

![Task 3 autonomous differential robot](https://github.com/Ahmed-M0ataz/autonomous_frist_pkg/media/mobile_robot.gif)

