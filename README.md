🤖 Autonomous Mobile Robot (AMR) NavigationDecodeLabs Industrial Training Kit | Project 3A practical ROS2-based system that gives a mobile robot spatial intelligence to map environments, find optimal paths, and avoid dynamic obstacles in real-time.💡 What Problem Does This Solve?Standard robots can only repeat fixed paths. When placed in real-world environments like warehouses, three major problems occur:Wheel Drift: Wheel encoders slip over time, causing the robot to lose track of where it is.Changing Obstacles: People, boxes, and forklifts move around, blocking static paths.Wall Collisions: Simple mathematical lines don't account for the robot's physical width.This project solves all three by fusing sensors to eliminate drift, planning paths around inflated obstacle borders, and dynamically stopping or re-routing when modern obstacles appear.⚙️ How It WorksThe robot operates on a continuous 3-step loop: Sense ➔ Plan ➔ Act.<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:12px; padding:10px; font-family:system-ui, sans-serif;">
  <!-- Perception Block -->
  <rect x="20" y="40" width="220" height="160" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="130" y="70" fill="#38bdf8" font-weight="bold" font-size="16" text-anchor="middle">1. PERCEPTION</text>
  <text x="130" y="95" fill="#94a3b8" font-size="13" text-anchor="middle">"Where am I?"</text>
  <path d="M 40 115 L 220 115" stroke="#334155" stroke-width="1"/>
  <text x="130" y="138" fill="#e2e8f0" font-size="12" text-anchor="middle">📡 LiDAR + Wheel Data</text>
  <text x="130" y="160" fill="#e2e8f0" font-size="12" text-anchor="middle">🧠 EKF Sensor Fusion</text>
  <text x="130" y="182" fill="#e2e8f0" font-size="12" text-anchor="middle">🗺️ 2D Occupancy Grid</text>

  <!-- Arrow 1 -->
  <path d="M 245 120 L 285 120" stroke="#38bdf8" stroke-width="3" fill="none" marker-end="url(#arrow)"/>

  <!-- Planning Block -->
  <rect x="290" y="40" width="220" height="160" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
  <text x="400" y="70" fill="#818cf8" font-weight="bold" font-size="16" text-anchor="middle">2. PLANNING</text>
  <text x="400" y="95" fill="#94a3b8" font-size="13" text-anchor="middle">"Where am I going?"</text>
  <path d="M 310 115 L 490 115" stroke="#334155" stroke-width="1"/>
  <text x="400" y="138" fill="#e2e8f0" font-size="12" text-anchor="middle">⭐ A* Search Algorithm</text>
  <text x="400" y="160" fill="#e2e8f0" font-size="12" text-anchor="middle">📏 Manhattan Heuristic</text>
  <text x="400" y="182" fill="#e2e8f0" font-size="12" text-anchor="middle">🛡️ Costmap Safety Buffer</text>

  <!-- Arrow 2 -->
  <path d="M 515 120 L 555 120" stroke="#818cf8" stroke-width="3" fill="none"/>

  <!-- Control Block -->
  <rect x="560" y="40" width="220" height="160" rx="10" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="670" y="70" fill="#4ade80" font-weight="bold" font-size="16" text-anchor="middle">3. ACTION</text>
  <text x="670" y="95" fill="#94a3b8" font-size="13" text-anchor="middle">"How do I get there?"</text>
  <path d="M 580 115 L 740 115" stroke="#334155" stroke-width="1"/>
  <text x="670" y="138" fill="#e2e8f0" font-size="12" text-anchor="middle">👀 Local Rolling Scanner</text>
  <text x="670" y="160" fill="#e2e8f0" font-size="12" text-anchor="middle">🛑 Smooth Deceleration</text>
  <text x="670" y="182" fill="#e2e8f0" font-size="12" text-anchor="middle">⚡ Motor Velocity Commands</text>
</svg>
The Step-by-Step BreakdownMapping & Position (Perception):Combines Wheel Encoders (movement) and IMU (rotation) using an Extended Kalman Filter (EKF) to stop positional drift.Uses LiDAR lasers to convert physical walls into a simple numerical map matrix:0: Safe open space100: Wall / Obstacle-1: Unexplored areaRoute Calculation (Global Planning):Uses the $A^*$ Algorithm with Manhattan distance to pick the shortest route on a grid.Inflation Layers: Expands wall boundaries mathematically so the robot doesn't scrape its edges while turning corners.Obstacle Avoidance (Local Control):Monitors a short-range "rolling window" around itself in real-time.If a person steps in front of the robot, a deceleration function ($tanh$) smoothly slows down or stops the motors before impact.🎯 Deliverables & Key Tasks[x] State Estimation: Filter raw sensor noise into clean position data (odom/filtered).[x] Custom Pathfinding: Write an $A^*$ search script tailored for 2D grid maps.[x] Dynamic Safety Override: Publish safe speed commands (Twist) that automatically slow down near obstacles.🔮 Future Scopes3D Visual SLAM: Upgrade from 2D LiDARs to RGB-D depth cameras for multi-floor mapping.Fleet Management: Coordinate multiple AMRs to work together in shared spaces without bumping into each other.AI Reinforcement Learning: Allow robots to predict human movements in busy hallways.📩 Contact & InfoProvider: DecodeLabsWebsite: decodelabs.techEmail: decodelabs.tech@gmail.com