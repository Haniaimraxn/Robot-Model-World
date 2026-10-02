# 🤖 Autonomous Mobile Robot (AMR) Navigation System

An intelligent, ROS2-powered spatial navigation platform designed to give mobile robots true autonomy in unpredictable environments[cite: 60, 62]. Instead of following hardcoded paths, this system enables a robot to map its surrounding world using LiDAR scans[cite: 60, 61], estimate its location accurately[cite: 64, 65], calculate optimal routes using $A^*$ search logic[cite: 61, 73], and dodge unexpected obstacles in real time[cite: 60, 61].

---

## 🏷️ Project Details
* **Project Name:** Project 3 - Autonomous Mobile Robot (AMR) Navigation[cite: 59, 61]
* **Program:** Industrial Training Kit (Batch 2026)[cite: 59]
* **Platform:** Powered by DecodeLabs[cite: 59]

---

## 📝 What Does It Do?

Rather than relying on fixed or repetitive movements[cite: 63], this system gives a wheeled robot complete spatial awareness to navigate through dynamic spaces[cite: 60, 61]. It solves three core problems in autonomous robotics[cite: 64]:

1. **Self-Location Tracking ("Where am I?"):** Fuses data from wheel encoders, IMU sensors, and 2D LiDAR to build a live map and know the robot's exact position without getting lost[cite: 64, 66, 68].
2. **Smart Route Calculation ("Where am I going?"):** Translates physical space into a grid matrix and calculates the safest, shortest path to a destination using mathematical pathfinding[cite: 69, 71, 74].
3. **Real-Time Obstacle Avoidance ("How do I avoid hitting walls?"):** Constantly checks a small moving window around the robot to detect new barriers and smoothly slows down or reroutes automatically[cite: 64, 78, 79].

---

## 🛠️ Key Technical Requirements & Features

* 🗺️ **LiDAR Occupancy Grid Mapping:** Converts raw laser scan ranges into a discrete 2D grid matrix ($0 = \text{Free Space}$, $100 = \text{Obstacle}$, $-1 = \text{Unexplored}$)[cite: 61, 69].
* 🎯 **Extended Kalman Filter (EKF) Sensor Fusion:** Merges noisy IMU readings and wheel odometry to eliminate wheel slip errors and positional drift[cite: 67, 68].
* 📐 **$A^*$ Pathfinding with Manhattan Heuristic:** Implements a priority-queue search algorithm using Manhattan distance to plan optimal 4-way grid routes[cite: 61, 74, 75].
* 🛡️ **Costmap Inflation Buffer:** Artificially expands wall boundaries in the digital map so the robot chassis never scrapes against real-world obstacles[cite: 76].
* ⚠️ **Smooth Hyperbolic Tangent ($\tanh$) Deceleration:** Dynamically scales motor speed based on obstacle proximity to ensure buttery-smooth braking instead of sudden jerks[cite: 79].

---

## 💻 Tech Stack & Frameworks

* 🤖 **Core Framework:** ROS2 (Robot Operating System 2)[cite: 62]
* 🗺️️ **Navigation & Mapping:** Nav2, SLAM / Gmapping Toolbox, `robot_localization`[cite: 62, 68, 70]
* 🎛️ **State Estimation:** Extended Kalman Filter (`ekf_localization_node`)[cite: 68, 70]
* 🖥️ **Simulation & Visualization:** Gazebo Simulator & RViz2[cite: 66, 80, 83]
* 🔢 **Coordinate Transformation:** TF2 Transform Trees (`map` $\rightarrow$ `odom` $\rightarrow$ `base_link`)[cite: 70, 82]

---

## ⚙️ How to Run (Commands to Start the Project)

Follow these terminal steps to configure your ROS2 workspace, build the project packages, and launch the navigation loop[cite: 81]:

### 1. Workspace Configuration & Setup
Open your terminal and source your base ROS2 installation, then clone and build the project repository:

```bash
# Source ROS2 Humble environment
source /opt/ros/humble/setup.bash

# Create workspace directory structure
mkdir -p ~/amr_ws/src
cd ~/amr_ws/src

# Clone the project source code
git clone [https://github.com/YOUR-USERNAME/amr_navigation.git](https://github.com/YOUR-USERNAME/amr_navigation.git)

# Build the workspace and source the overlay
cd ~/amr_ws
colcon build --symlink-install
source install/setup.bash