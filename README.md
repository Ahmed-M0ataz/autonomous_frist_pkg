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

## Steps to Create a URDF File

Follow these steps to create a URDF file for your differential robot:

1. **Create a ROS Package**

   If you haven't already set up a ROS workspace and package, you can create one by referring to the official ROS tutorial mentioned in the prerequisites.

2. **Create a URDF Folder**

   Inside your ROS package directory, create a folder named `urdf`. This folder will be used to store your URDF files.

3. **Create a URDF File**

   Inside the `urdf` folder, create a new file with the extension `.xacro`. You can choose any name for this file, but for this example, let's name it `file.xacro`. You can write your robot's URDF description in this file by following the guidelines provided in the [official ROS URDF tutorial](http://wiki.ros.org/urdf/Tutorials).

## Example Folder Structure

Your ROS package directory should now resemble the following structure:

