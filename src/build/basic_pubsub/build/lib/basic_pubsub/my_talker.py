import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyTalker(Node):
    def __init__(self):
        super().__init__('my_talker')

        self.publisher = self.create_publisher(
            String,
            '/edward_chatter',
            10
        )

        self.count = 0

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

    def publish_message(self):
        msg = String()
        msg.data = f'Hello from Edward: {self.count}'

        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

        self.count += 1


def main(args=None):
    rclpy.init(args=args)

    node = MyTalker()

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
