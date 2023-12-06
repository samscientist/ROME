### Activate RPLiDAR S2 - on ROS2


```bash
sudo apt update
sudo apt install python3-colcon-common-extensions
```
[](https://colcon.readthedocs.io/en/released/user/installation.html)

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

```bash
git clone https://github.com/Slamtec/sllidar_ros2.git
cd ~/ros2_ws/
source /opt/ros/<rosdistro>/setup.bash
colcon build --symlink-install
```


```bash
# .../ros2_ws/ >
source ./install/setup.bash

sudo chmod 777 /dev/ttyUSB0
ros2 launch sllidar_ros2 view_sllidar_s2_launch.py
```

### SLAM

**Check if Cartographer is installed**
```bash
source ros2 pkg list | grep cartographer
```

**Install Cartographer**
```bash
sudo apt install ros-foxy-cartographer-ros
```
