import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/c/Users/Edward/workspaces/robotics-portfolio/ros2-vision-perception/src/install/basic_pubsub'
