# 🤖 Project 3 - Autonomous Mobile Robot (AMR) Navigation

An intelligent, ROS2-powered spatial navigation platform designed to give mobile robots true autonomy in unpredictable environments. Instead of following hardcoded paths, this system enables a robot to map its surrounding world using LiDAR scans, estimate its location accurately, calculate optimal routes using $A^*$ search logic, and dodge unexpected obstacles in real time.

---

## 🏷️ Project Details
* **Project Name:** Project 3 - Autonomous Mobile Robot (AMR) Navigation
* **Program:** Industrial Training Kit (Batch 2026)
* **Platform:** Powered by DecodeLabs

---

## 📝 What Does It Do?

Rather than relying on fixed or repetitive movements, this system gives a wheeled robot complete spatial awareness to navigate through dynamic spaces. It solves three core problems in autonomous robotics:

1. **Self-Location Tracking ("Where am I?"):** Fuses data from wheel encoders, IMU sensors, and 2D LiDAR to build a live map and know the robot's exact position without getting lost.
2. **Smart Route Calculation ("Where am I going?"):** Translates physical space into a grid matrix and calculates the safest, shortest path to a destination using mathematical pathfinding.
3. **Real-Time Obstacle Avoidance ("How do I avoid hitting walls?"):** Constantly checks a small moving window around the robot to detect new barriers and smoothly slows down or reroutes automatically.

---

## 🛠️ Key Technical Requirements & Features

* 🗺️ **LiDAR Occupancy Grid Mapping:** Converts raw laser scan ranges into a discrete 2D grid matrix ($0 = \text{Free Space}$, $100 = \text{Obstacle}$, $-1 = \text{Unexplored}$).
* 🎯 **Extended Kalman Filter (EKF) Sensor Fusion:** Merges noisy IMU readings and wheel odometry to eliminate wheel slip errors and positional drift.
* 📐 **$A^*$ Pathfinding with Manhattan Heuristic:** Implements a priority-queue search algorithm using Manhattan distance to plan optimal 4-way grid routes.
* 🔵 **Costmap Inflation Buffer:** Artificially expands wall boundaries in the digital map so the robot chassis never scrapes against real-world obstacles.
* ⚠️ **Smooth Hyperbolic Tangent ($\tanh$) Deceleration:** Dynamically scales motor speed based on obstacle proximity to ensure buttery-smooth braking instead of sudden jerks.

---

## 💻 Tech Stack & Frameworks

* 🤖 **Core Framework:** ROS2 (Robot Operating System 2)
* 🗺️ **Navigation & Mapping:** Nav2, SLAM / Gmapping Toolbox, `robot_localization`
* 🎛️ **State Estimation:** Extended Kalman Filter (`ekf_localization_node`)
* 🖥️ **Simulation & Visualization:** Gazebo Simulator & RViz2
* 🔢 **Coordinate Transformation:** TF2 Transform Trees (`map` $\rightarrow$ `odom` $\rightarrow$ `base_link`)

---

## ⚙️ How to Run (Commands to Start the Project)

Follow these terminal steps to configure your ROS2 workspace, build the project packages, and launch the navigation loop:

### 1. Workspace Configuration & Setup
Open your terminal and source your base ROS2 installation, then clone and build the project repository:

```bash
# Source ROS2 Humble environment
source /opt/ros/humble/setup.bash

# Create workspace directory structure
mkdir -p ~/amr_ws/src
cd ~/amr_ws/src

# Clone the project source code
git clone [https://github.com/Haniaimraxn/Robot-Model-World.git](https://github.com/Haniaimraxn/Robot-Model-World.git)

# Build the workspace and source the overlay
cd ~/amr_ws
colcon build --symlink-install
source install/setup.bash