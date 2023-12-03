import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

import Adafruit_PCA9685
pca = Adafruit_PCA9685.PCA9685(i2c, address=0x70)
pca.frequency = 1600
