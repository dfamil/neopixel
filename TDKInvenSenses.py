import time
import board
import adafruit_icm20x
class TDKInvenSenses:
    def __init__(self):
        i2c = board.I2C()
        self.icm = adafruit_icm20x.ICM20948(i2c)
        self.text = ""
    def update(self,type):
        self.type = type
        if self.type == "acceleration":
            #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (self.icm.acceleration))
            self.text = "%.2f, %.2f, %.2f" % (self.icm.acceleration) # overly long to see where it clips
        elif self.type == "magnetic":
            #print("Mag: %.2f, %.2f, %.2f, uT" % (self.icm.magnetic) )# overly long to see where it clips
            self.text = "%.2f, %.2f, %.2f" % (self.icm.magnetic) # overly long to see where it clips
        else:
            #print("Gyro: %.2f, %.2f, %.2f, uT" % (self.icm.gyro) )# overly long to see where it clips
            self.text = "%.2f, %.2f, %.2f" % (self.icm.gyro) # overly long to see where it clips
    def returnText(self):
        #print(self.text)
        return self.text
