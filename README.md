# nitinscodehub-ROS-Navigation-Challenge-CUJammu-2025

# 🏆 ROS Navigation Challenge 2024 - Team Hackers CUJammu

![Rulebook Compliant](https://img.shields.io/badge/Rulebook-100%25_Compliant-green)
![ROS Version](https://img.shields.io/badge/ROS-Noetic-blue)

## 🚀 Team Members
| Name              | Email                          | Role                |
|-------------------|--------------------------------|---------------------|
| Nitin Dhurve      | ni23beccs33@cujammu.ac.in      | Path Planning (A*)  |
| Abhishek Maurya   | abhishekmaurya102515k@gmail.com| DWA Controller      |
| Abhay             | emailtoabhay01@gmail.com       | Sensor Integration  |

## 📜 Rulebook Compliance
✔ Uses only permitted sensors (Lidar + Odometry)  
✔ Auto-recovery within 30s (Section 2.3)  
✔ Two-attempt scoring system implemented  

## 💻 How to Run
```bash
catkin_make
source devel/setup.bash
roslaunch gazebo_ros maze_world.launch
roslaunch hackers_cujammu main.launch
