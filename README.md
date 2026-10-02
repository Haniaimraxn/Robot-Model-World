# 🤖 Autonomous Mobile Robot (AMR) Navigation

## 📖 Description

This project provides a ROS2-based spatial intelligence system for an Autonomous Mobile Robot (AMR)[cite: 30, 31]. It enables the robot to autonomously map unknown physical environments, generate optimal global routes, and dynamically avoid obstacles in real time[cite: 30].

* **Perception & Mapping:** Fuses raw wheel odometry and IMU data using an **Extended Kalman Filter (EKF)** to eliminate drift[cite: 37], while processing LiDAR laser scans to construct a 2D Occupancy Grid map[cite: 30, 35].
* **Global Pathfinding:** Implements the **A* Search Algorithm** with a Manhattan distance heuristic to calculate collision-free paths around inflated obstacle borders[cite: 42, 43, 45].
* **Local Obstacle Avoidance:** Continuously monitors a short-range local costmap rolling window[cite: 47] and executes smooth deceleration using hyperbolic tangent (`tanh`) velocity scaling when dynamic obstacles appear[cite: 48].

---

## 🚀 How to Run

### 1. Prerequisites & Setup
Ensure ROS2 and the necessary navigation stack packages are installed, then source your workspace:

```bash
# Source ROS2 installation
source /opt/ros/humble/setup.bash

# Clone and build the workspace
mkdir -p ~/amr_ws/src
cd ~/amr_ws/src
git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git) amr_navigation
cd ~/amr_ws
colcon build --symlink-install
source install/setup.bash