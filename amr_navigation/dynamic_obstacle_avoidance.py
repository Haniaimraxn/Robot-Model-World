import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

class DynamicObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('dynamic_obstacle_avoidance')
        self.sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.max_speed = 0.5
        self.safe_distance = 0.8

    def scan_callback(self, msg):
        if not msg.ranges:
            return

        min_dist = min([r for r in msg.ranges if not math.isnan(r) and r > 0.05], default=10.0)
        twist = Twist()

        # PDF Smooth Hyperbolic Tangent Deceleration Formula
        if min_dist < self.safe_distance:
            twist.linear.x = self.max_speed * math.tanh(min_dist)
            twist.angular.z = 0.5
        else:
            twist.linear.x = self.max_speed
            twist.angular.z = 0.0

        self.pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = DynamicObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()