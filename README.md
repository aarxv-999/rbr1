# 6-DOF Robotic Arm
this is a project in micropython so as to control the 6 degree of freedom robotic arm with raspberry pi pico and the PCA9685 PWM controller


# list of hardware
raspberry pi pico <br/>
PCA9685 16 channel pwm controller <br/>
3 IDUINO Rds3235 servos (for the angle based movement) <br/>
3 MG996r servis (for continuous rotational movement) <br/>
power supply - 5v for servos and 3.3v for pico <br/>

# wiring
PCA9685 sda to pico GPIO 0 <br/>
PCA9685 SCL to PICO GPIO 1 <br/>
PCA0685 VCC to 3.3v and V+ to 5v for servos <br/>
servos connected to PCA9685 channels 0 through 5 <br/>
common grounds for pico pca9685 and servos <br/>

# servo to joint mapping
channel 0 - base <br/>
channel 1 - shoulder <br/>
channel 2 - elbow <br/>
channel 3 - wrist pitch <br/>
channel 4: wrist rotate <br/>
channel 5: gripper <br/>


# how to run 
upload all the .py files to pico <br/>
run main.py <br/>
either choose manual test or task mode <br/>


to test servos run manual test to individually test the servos then select a channel from 0 to 5 and make it clear whether it is an angle based action or continuous if it is angle based then enter the angle or else the direction

