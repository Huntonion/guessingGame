![](https://github.com/Huntonion/guessingGame/blob/main/media/turtle.gif)

# Guessing Game


This is a project involving a robot called turtlebot3 that utilizes ROS to recognize human speech and act according to certain input phrases. 

## Requirements

- Ubuntu 20.04
- ROS Noetic 
- Vosk (https://github.com/alphacep/ros-vosk)
- turtlebot3 (please follow the guide on https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/ on how to setup turtlebot3)



## Installation

first clone the git
```
git clone https://github.com/Huntonion/guessingGame.git
```

then position yourself into your catkin workspace and run `catkin_make`

## Running

To get it working, just run the various nodes:

`roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

`roslaunch turtlebot3_example interactive_markers.launch`

`rosrun ros_vosk vosk_node.py`

`rosrun guessingGame guessingGame.py`

`rosrun guessingGame movement.py`

`rosrun guessingGame dance.py`

Then, the user can engage in a minigame by telling the robot phrases such as "Turtle, start the guessing game." or can order the robot to dance and move by saying "Turtle, move forward" and "Turtle, dance".
