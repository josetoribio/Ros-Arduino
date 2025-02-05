import rclpy
from rclpy.node import Node
import serial 
import time
from std_msgs.msg import String


class ServoPublisher(Node):

    def __init__(self):
        
        super().__init__('Servo_publisher')
        self.publisher_ = self.create_publisher(String, 'Servo', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        ser = serial.Serial(port='/dev/ttyACM0',baudrate=115200, timeout=.1) 
        time.sleep(0.05)  # Give Arduino time to initialize
        msg = String()
        string_to_send = input("Turn On or Off the SERVO: ")
        ser.write(string_to_send.encode('utf-8'))  # Encode the string to bytes
        msg.data = 'ServoMode:'+string_to_send 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
	    
        


def main(args=None):
    rclpy.init(args=args)

    Servo_publisher = ServoPublisher()

    rclpy.spin(Servo_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    Servo_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
