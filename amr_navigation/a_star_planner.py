import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped
import heapq

class AStarPlanner(Node):
    def __init__(self):
        super().__init__('a_star_planner')
        self.subscription = self.create_subscription(
            OccupancyGrid, '/map', self.map_callback, 10
        )
        self.publisher_ = self.create_publisher(Path, '/plan', 10)
        self.get_logger().info('A* Path Planner Node Initialized')

    def manhattan_distance(self, p1, p2):
        # Strict Manhattan Distance Heuristic: |x1 - x2| + |y1 - y2|
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def map_callback(self, msg):
        grid = msg.data
        width = msg.info.width
        height = msg.info.height
        
        # Example Start and Goal coordinates in grid indices
        start = (0, 0)
        goal = (width - 1, height - 1)

        path = self.a_star_search(grid, width, height, start, goal)
        if path:
            self.publish_path(path, msg.info)

    def a_star_search(self, grid, width, height, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.manhattan_distance(start, goal)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            # 4-directional grid neighbors
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in neighbors:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < width and 0 <= neighbor[1] < height:
                    index = neighbor[1] * width + neighbor[0]
                    # Check if space is free (0 = free space)
                    if grid[index] == 0:
                        tentative_g = g_score[current] + 1
                        if neighbor not in g_score or tentative_g < g_score[neighbor]:
                            came_from[neighbor] = current
                            g_score[neighbor] = tentative_g
                            f = tentative_g + self.manhattan_distance(neighbor, goal)
                            f_score[neighbor] = f
                            heapq.heappush(open_set, (f, neighbor))
        return None

    def publish_path(self, path_coords, map_info):
        path_msg = Path()
        path_msg.header.frame_id = 'map'
        path_msg.header.stamp = self.get_clock().now().to_msg()

        for col, row in path_coords:
            pose = PoseStamped()
            pose.header = path_msg.header
            pose.pose.position.x = col * map_info.resolution + map_info.origin.position.x
            pose.pose.position.y = row * map_info.resolution + map_info.origin.position.y
            path_msg.poses.append(pose)

        self.publisher_.publish(path_msg)

def main(args=None):
    rclpy.init(args=args)
    node = AStarPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()