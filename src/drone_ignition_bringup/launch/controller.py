import time

import rclpy
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Path
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, QoSProfile
from sensor_msgs.msg import PointCloud2
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
    
    
    def rviz_goal_callback(self, msg):
        """Go to the goal provided by the clicked_point in RViz"""

        self.get_logger().warn('New goal from RViz')
        goal_xy = self.map_.world_to_pixel(msg.point.x, msg.point.y)

        # Clear visualised path and search markers
        empty_path = Path()
        empty_path.header.frame_id = 'map'
        self.path_pub_.publish(empty_path)
        self.path_smooth_pub_.publish(empty_path)

        # Start planning
        self.plan_path(goal_xy)