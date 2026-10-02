import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    package_name = 'amr_navigation'
    pkg_share = get_package_share_directory(package_name)

    # File paths
    xacro_file = os.path.join(pkg_share, 'urdf', 'amr_robot.urdf.xacro')
    world_file = os.path.join(pkg_share, 'worlds', 'maze_world.world')
    ekf_config = os.path.join(pkg_share, 'config', 'ekf.yaml')

    # Process URDF/XACRO file
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}

    # 1. Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': True}]
    )

    # 2. Gazebo Simulator
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': world_file}.items()
    )

    # 3. Spawn Robot in Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'amr_robot'],
        output='screen'
    )

    # 4. Extended Kalman Filter Node (robot_localization)
    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[ekf_config, {'use_sim_time': True}]
    )

    # 5. Custom A* Pathfinding Node
    a_star_node = Node(
        package='amr_navigation',
        executable='a_star_planner',
        name='a_star_planner',
        output='screen'
    )

    # 6. Dynamic Obstacle Avoidance Node
    obstacle_avoidance_node = Node(
        package='amr_navigation',
        executable='dynamic_obstacle_avoidance',
        name='dynamic_obstacle_avoidance',
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher_node,
        spawn_entity,
        ekf_node,
        a_star_node,
        obstacle_avoidance_node
    ])