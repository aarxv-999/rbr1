# 6-DOF Robotic Arm
this is a project in micropython so as to control the 6 degree of freedom robotic arm with raspberry pi pico and the PCA9685 PWM controller


# list of hardware
raspberry pi pico
PCA9685 16 channel pwm controller
3 IDUINO Rds3235 servos (for the angle based movement)
3 MG996r servis (for continuous rotational movement)
power supply - 5v for servos and 3.3v for pico

# wiring
PCA9685 sda to pico GPIO 0 
PCA9685 SCL to PICO GPIO 1
PCA0685 VCC to 3.3v and V+ to 5v for servos 
servos connected to PCA9685 channels 0 through 5 
common grounds for pico pca9685 and servos 

# servo to joint mapping
channel 0 - base
channel 1 - shoulder 
channel 2 - elbow 
channel 3 - wrist pitch
channel 4: wrist rotate 
channel 5: gripper 


# how to run 
upload all the .py files to pico 
run main.py
either choose manual test or task mode 


to test servos run manual test to individually test the servos then select a channel from 0 to 5 and make it clear whether it is an angle based action or continuous if it is angle based then enter the angle or else the direction

