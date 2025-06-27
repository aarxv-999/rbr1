# servo channels assignment
BASE = 0
SHOULDER = 1
ELBOW = 2
WRIST_PITCH = 3
WRIST_ROTATE = 4
GRIPPER = 5

# angle based servo limits in degrees
ANGLE_MIN = 0
ANGLE_MAX = 180

#continuous servo pwm values
NEUTRAL_PWM = 300 # 1.5ms, stop
CW_SLOW = 360 # 1.8ms, clockwise
CCW_SLOW = 240 # 1.2ms, counterclockwise
