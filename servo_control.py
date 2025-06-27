from machine import I2C, Pin
import time
import ustruct

class ServoController:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
        self.PCA9685_ADDR = 0x40
        self._write_reg(0x00, 0x00)  # resetting it
        self._write_reg(0x01, 0x04)  # sleep
        self.set_freq(50)  #50 Hz for servos
        self._write_reg(0x01, 0x00)  # wake up

    def set_freq(self, freq):
        prescale = int(25000000 / (4096 * freq) - 1)
        self._write_reg(0xFE, prescale)

    def _write_reg(self, reg, value):
        self.i2c.writeto_mem(self.PCA9685_ADDR, reg, bytes([value]))

    def _set_pwm(self, channel, on, off):
        base = 0x06 + 4 * channel
        self.i2c.writeto_mem(self.PCA9685_ADDR, base, ustruct.pack("<HH", on, off))

    def set_angle(self, channel, angle):
        if angle < 0:
            angle = 0
        if angle > 180:
            angle = 180
        pulse = 500 + (angle * 2000) // 180  # 500-2500us for 0-180 deg
        pwm_val = int(pulse * 4096 / 20000)  # scale to 12-bit
        self._set_pwm(channel, 0, pwm_val)

    def rotate_servo(self, channel, direction):
        if direction == "clockwise":
            pwm_val = 360  # around 1.8ms pulse
        elif direction == "counterclockwise":
            pwm_val = 240  # around 1.2ms pulse
        else:  # stop
            pwm_val = 300  # around 1.5ms pulse
        self._set_pwm(channel, 0, pwm_val)
