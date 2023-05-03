# Control TurtleBot3 in Gazebo with Hand Gesture Detection #


### Requirements (Tested Version) ###
* Ubuntu 20.04 Focal Fossa  
* ROS Noetic  
* Python 3.8  
* opencv-python 4.5.5.64  
* cvzone 1.4.1  
* mediapipe 0.8.7.1  
* protobuf 3.20.x or lower

<br/>

### Installation & Launch ###
**Install:**
```
cd ~/catkin_ws/src/
```
```
git clone https://github.com/kkr0913/ROS_GestureControl.git
```
```
gedit ~/.bashrc
```
Add this line at the bottom of the file:
```
export TURTLEBOT3_MODEL=burger
```
Save and close the file.
```
source ~/.bashrc
```
```
cd ~/catkin_ws && catkin_make
```

<br/>

**Launch:**
```
roslaunch control main.launch
```

<br/><br/><br/>

<p float="left">
  <img src="/image/screenshot.png" height="300" />
  &nbsp;
  <img src="/image/hand.png" height="300" /> 
</p>

<br/><br/>

### Reference ###
[https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation)  
[https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/](https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/)
