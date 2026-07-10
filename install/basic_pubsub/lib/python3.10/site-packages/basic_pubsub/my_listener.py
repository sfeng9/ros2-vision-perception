import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyListener(Node):
    def __init__(self):
        super().__init__('my_listener')

        self.subscription = self.create_subscription(
            String,
            '/edward_chatter',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    node = MyListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()