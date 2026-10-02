🤖 Autonomous Mobile Robot (AMR) Navigation SystemAn edge-compatible Spatial Intelligence & Autonomous Navigation Platform built for real-time mobile robot mapping, optimal path planning, and dynamic obstacle avoidance in ROS2. The system seamlessly connects sensor data to robot movement using Extended Kalman Filtering (EKF), 2D LiDAR SLAM, occupancy grid pathfinding, and smooth velocity-scaling feedback loops.🏷️ System ClassificationROS2 Spatial Intelligence & Dynamic Navigation Control Pipeline📝 Overview & Core FunctionalityThe Autonomous Mobile Robot (AMR) Navigation System is a low-latency spatial intelligence system designed for smooth, reliable, and fully autonomous movement through unknown or changing environments.Using a continuous state-estimation pipeline, the system reads raw wheel odometry, IMU data, and 2D LiDAR scans to construct a live Occupancy Grid map on the fly. It plans collision-free paths using modified graph search and dynamically scales motor speed (cmd_vel) to dodge unexpected obstacles smoothly without any manual control.🛠️ Architecture & System Workflow┌─────────────────────────────────────────────────────────┐
│         📡 Sensor Inputs (LiDAR + Odometry + IMU)       │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│           🔍 Phase 1: Environment & State               │
├─────────────────────────────────────────────────────────┤
│  ├─ Extended Kalman Filter (EKF Drift Correction)       │
│  └─ 2D Occupancy Grid Mapping                           │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│             📐 Phase 2: Path Generation                 │
├─────────────────────────────────────────────────────────┤
│  ├─ A* Search Algorithm (Manhattan Distance)            │
│  └─ Costmap Inflation & Trajectory Generation           │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│           🤖 Phase 3: Dynamic Motion Control            │
├─────────────────────────────────────────────────────────┤
│  ├─ Rolling Local Costmap Window                        │
│  └─ Velocity Scaling (tanh Smooth Deceleration)         │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            ⚙️ Motor Command Output: cmd_vel             │
└─────────────────────────────────────────────────────────┘
📡 Phase 1 — Environment Sensing & State Tracking🎥 Multi-Sensor Fusion: Seamlessly synchronizes raw wheel encoders, 9-DOF IMU telemetry, and 2D LiDAR point clouds at high loop rates.🎯 EKF State Estimation: Runs an Extended Kalman Filter (EKF) to blend odometry and inertial data, eliminating cumulative drift caused by wheel slips.📦 2D Occupancy Grid Mapping: Converts raw laser scan returns into clear 2D probability grid maps showing open space, obstacles, and unexplored areas.📐 Phase 2 — Path Calculation & Route Planning🔍 A Trajectory Planning:* Evaluates the occupancy grid using an A Search Algorithm* tuned with a Manhattan distance heuristic for optimal routing.🛡️ Safety Inflation Margins: Adds intelligent buffer zones around obstacle borders to match the robot’s physical footprint and prevent close calls.🔄 Coordinate Translation: Swiftly converts real-world spatial coordinates into grid matrix values for fast path calculations.⚙️ Waypoint Sequence Generation: Creates a structured list of spatial waypoints ($W_1 \dots W_n$) that guide the robot smoothly from start to goal.🤖 Phase 3 — Real-Time Obstacle Avoidance & Drive Control📈 Local Area Monitoring: Continuously checks a moving local sub-grid right around the robot to detect sudden, unmapped obstacles.📊 Speed & Direction Control: Calculates real-time linear ($v_x$) and angular ($\omega_z$) motor speed commands published directly to the cmd_vel ROS2 topic.⚠️ Smooth Deceleration: Uses a hyperbolic tangent ($\tanh$) mathematical curve for buttery-smooth slowing down or re-routing when obstacles pop up.🖥️ Live Telemetry Visualization: Streams real-time TF transform trees, costmap overlays, and path vectors directly to RViz2 for quick debugging and monitoring.💻 Tech Stack & Tools🤖 ROS2 (Robot Operating System 2): Core modular framework using nodes, topics, services, and actions for asynchronous communication.🐍 Python 3.10+ / C++17: Runtimes powering mathematical navigation nodes and high-frequency sensor processing.🔢 NumPy & Eigen: Handles fast matrix calculations, spatial coordinate transformations, and vector math.🗺️ Nav2 & SLAM Toolbox: Powers occupancy grid mapping, costmap lifecycle management, and spatial transform broadcasting (tf2).🖥️ Gazebo & RViz2: High-fidelity 3D physics simulator paired with real-time visualization viewports.🏭 Design Purpose & Practical Applications⚡ Predictable & Safe Motion: Pairs global route planning with local velocity damping ($\tanh$) to ensure controlled, natural movement without sudden jerks.📏 Accurate Spatial Mapping: Converts raw laser ranges into distinct occupancy values across active local and global costmap grids.🌐 Flexible Hardware Integration: Built to run seamlessly inside Gazebo simulation environments or deploy directly onto physical ROS2 differential-drive robots and industrial AGVs.🚀 Setup & Execution GuideFollow these steps to set up your ROS2 workspace and run the navigation pipeline:1. Workspace Configuration# Source base ROS2 distribution
source /opt/ros/humble/setup.bash

# Create workspace directory structure
mkdir -p ~/amr_ws/src
cd ~/amr_ws/src

# Clone the project repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git amr_navigation

# Build workspace and source overlay
cd ~/amr_ws
colcon build --symlink-install
source install/setup.bash
2. Launch SequenceOpen a new sourced terminal tab for each step:Step 1: Start Gazebo Simulation & EKF Noderos2 launch amr_navigation simulation_ekf.launch.py
Step 2: Start SLAM Mapping Noderos2 launch amr_navigation slam_mapping.launch.py
Step 3: Run A Path Planner Node*ros2 run amr_navigation a_star_planner
Step 4: Start Obstacle Avoidance Controllerros2 run amr_navigation dynamic_avoidance_node
