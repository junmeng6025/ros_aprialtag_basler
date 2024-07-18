# ros_apriltag_basler

## Getting started
Follow the steps in [BASLER setup](basler_setup.md) to ensure the BASLER camera can send video stream to PC successfully.

## Build the ROS workspace
```bash
cd ros_apriltag_basler/catkin_ws
catkin build
```
## Connect the cables
Connect the power cable and the data cable correctly. Check the connection by launching the script `basler_detect.py` in the directory `catkin_ws/src/apriltag_pose/scripts`. If that works, you can continue with the following steps.
> Might doesn't work when called from terminal.  
> try to open the project in VSCode and launch the script by hitting the `run` button

## Launch the detect node 
```bash
cd ros_apriltag_basler/catkin_ws
source devel/setup.bash
```
### Option A: All in one node
```bash
roslaunch apriltag_pose ap_detect_in_one.launch
```
Image acquisition and AprilTag detection processed in the same ROS node  
- \+ Good synchronized visualization
- \- Low FPS, ca. 9 fps

> If you need the log saved:
> ```bash
> roslaunch apriltag_pose ap_detect_in_one.launch > output.log 2>&1
> ```
The log will be saved in folder `catkin_ws`

### Option B: Image getting and AprilTag detection separated
```bash
roslaunch apriltag_pose basler_detect.launch
```
Image acquisition and AprilTag detection processed in different ROS nodes, feasible for further develop with other cameras, eg Webcam.  
- \+ High FPS, ca. 30 fps
- \- Bad synchronized visualization. Visualization ca. 0.5s lag after the movement
### To Monitor the content of `/poses`
```bash
rostopic echo /poses
```
