import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

class DynamicObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('dynamic_obstacle_avoidance')
        self.scan_sub = self.create_subscription(
            LaserScan, '/scan', self.scan_callback, 10
        )
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.target_speed = 0.5  # Max desired speed (m/s)
        self.safe_distance = 1.5 # Distance where deceleration begins (meters)
        self.get_logger().info('Dynamic Obstacle Avoidance Node Initialized')

    def scan_callback(self, msg):
        # Extract minimum distance in front of the robot (-30 deg to +30 deg)
        num_readings = len(msg.ranges)
        front_angle_range = int(num_readings * (30 / 360))
        
        front_ranges = (
            msg.ranges[:front_angle_range] + 
            msg.ranges[-front_angle_range:]
        )
        
        # Filter out inf / zero values
        valid_ranges = [r for r in front_ranges if msg.range_min < r < msg.range_max]
        
        if not valid_ranges:
            return
            
        min_dist = min(valid_ranges)
        
        # Hyperbolic tangent (\tanh) deceleration curve calculation
        # Scale speed between 0.0 and target_speed based on obstacle distance
        linear_vel = self.target_speed * math.tanh(min_dist / self.safe_distance)
        
        # Emergency stop if obstacle is closer than 0.2 meters
        if min_dist < 0.2:
            linear_vel = 0.0

        cmd_msg = Twist()
        cmd_msg.linear.x = float(linear_vel)
        cmd_msg.angular.z = 0.0
        
        self.cmd_pub.publish(cmd_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DynamicObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()