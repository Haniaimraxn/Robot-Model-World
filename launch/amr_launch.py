import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_amr = FindPackageShare('amr_navigation')

    world_path = PathJoinSubstitution([pkg_amr, 'worlds', 'maze_world.sdf'])
    urdf_path = PathJoinSubstitution([pkg_amr, 'urdf', 'amr_robot.urdf'])

    return LaunchDescription([
        # 1. Gazebo Simulation World Launch
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-world', 'default',
                '-file', urdf_path,
                '-name', 'amr_robot',
                '-x', '0.0', '-y', '0.0', '-z', '0.1'
            ],
            output='screen'
        ),

        # 2. ROS GZ Bridge for LiDAR & Cmd_Vel
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
                '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
                '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
                '/imu@sensor_msgs/msg/Imu@gz.msgs.IMU'
            ],
            output='screen'
        ),

        # 3. EKF Localization Node (PDF Page 30 Requirement)
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[PathJoinSubstitution([pkg_amr, 'config', 'ekf.yaml'])]
        ),

        # 4. Custom A* Pathfinding Node
        Node(
            package='amr_navigation',
            executable='a_star_planner',
            name='a_star_planner',
            output='screen'
        ),

        # 5. Dynamic Obstacle Avoidance Node
        Node(
            package='amr_navigation',
            executable='dynamic_obstacle_avoidance',
            name='dynamic_obstacle_avoidance',
            output='screen'
        )
    ])