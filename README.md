# Guessing Game

This is a project involing a robot called Link that utilizes ROS to recognize human speech and act according to certain input phrases. 

## Installation

first clone the git
```
https://github.com/Huntonion/guessingGame.git
```
this application depends on vosk to recognize speech, therefore installing vosk is necessary, so just follow the steps at https://github.com/alphacep/ros-vosk to get it working.

then position yourself into your catkin workspace and run `catkin_make`

## Running

To get it working, just run the various nodes:

`rosrun guessingGame guessingGame.py`

`rosrun guessingGame movement.py`

`rosrun guessingGame dance.py`

`rosrun ros_vosk vosk_node.py`

Then, the user can engage in a minigame by telling the robot phrases such as "Link, start the guessing game." or can order the robot to dance and move by saying "Link, come here" and "Link, dance".
