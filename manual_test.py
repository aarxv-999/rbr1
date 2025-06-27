from servo_controller import ServoController
from config import *

controller = ServoController()

def test_servo():
    print("Enter servo channel (0-5):")
    channel = int(input())
    if channel < 0 or channel > 5:
        print("Invalid channel!")
        return
    print("Is it angle-based (a) or continuous (c)?")
    servo_type = input().lower()
    if servo_type == 'a':
        print("Enter angle (0-180):")
        angle = int(input())
        controller.set_angle(channel, angle)
        print(f"Set channel {channel} to {angle} degrees")
    elif servo_type == 'c':
        print("Enter direction (clockwise, counterclockwise, stop):")
        direction = input().lower()
        controller.rotate_servo(channel, direction)
        print(f"Set channel {channel} to {direction}")
    else:
        print("Invalid servo type!")

while True:
    test_servo()
    print("Test another? (y/n)")
    if input().lower() != 'y':
        break
