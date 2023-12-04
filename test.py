import board
import busio
import time

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_pca9685
pca = adafruit_pca9685.PCA9685(i2c, address=0x40)
pca.frequency = 1600

from adafruit_motor import motor
pwm_channel = pca.channels[0]
#channel1 = pca.channels[0]
#channel2 = pca.channels[9]
pwm_channel.duty_cycle = 0x0050 # hold high

#motor1 = motor.DCMotor(channel1, channel2)

# from adafruit_servokit import ServoKit
# myKit=ServoKit(channels=16)
# myKit.servo[0].angle=0
# time.sleep(5)
# myKit.servo[1].angle=90
# time.sleep(5)
# myKit.servo[0].angle=180