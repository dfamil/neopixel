import board
import displayio
import terminalio
import time
import adafruit_icm20x
import gc
import Mapping
# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9
positionAcceList = []
positionGyroList = []
positionMagList = []

# Use for I2C
i2c = board.I2C()
icm = adafruit_icm20x.ICM20948(i2c)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

# Make the display context
splash = displayio.Group()
display.show(splash)


text1=0
text1 = "1%.2f, %.2f, %.2f m/s^2" % (icm.acceleration) # overly long to see where it clips
text2 = "2%.2f, %.2f, %.2f m/s^2" % (icm.magnetic) # overly long to see where it clips
text3 = "3%.2f, %.2f, %.2f m/s^2" % (icm.gyro) # overly long to see where it clips
text_area1 = label.Label(terminalio.FONT, text=str(text1),  scale=1, color=0xFFFFFF, x=8, y=8)
splash.append(text_area1)

text_area2 = label.Label(terminalio.FONT, text=str(text2),  scale=1, color=0xFFFFFF, x=8, y=25)
splash.append(text_area2)

text_area3 = label.Label(terminalio.FONT, text=str(text3),  scale=1, color=0xFFFFFF, x=8, y=43)
splash.append(text_area3)
def maprange( a, b, s):
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
 
for s in range(1):
    print("%g maps to %g" % (s, maprange( (-52.27,11.96), (0, 255), s)))
    print("%g maps to %g" % (-52.27, maprange( (-52.27,11.96), (0, 800), -52.27)))
    print("%g maps to %g" % (11.96, maprange( (-52.27,11.96), (0, 800), 11.96)))
    
 
print("test")


  # accel
    # max [[11.96, 21.97, 24.52]]
    # min [[-52.27, -78.45, -34.66]]
    # gyro
    # max [[65.4, 73.95, 49.65]]
    # min [[-12.6, -24.75, -43.35]]
    # mag
    # max [[8.73, 8.73, 8.73]]
    # min [[-8.73, -8.73, -8.73]]       

lenList = 0
list2 = [-8.61, -8.57, -8.55, -8.51]
print(max(list2))
while True:
    text1 = "%.2f, %.2f, %.2f, m/s^2" % (icm.acceleration) # overly long to see where it clips
    text2 = "%.2f, %.2f, %.2f, uT" % (icm.magnetic) # overly long to see where it clips
    text3 = "%.2f, %.2f, %.2f, rads/s" % (icm.gyro) # overly long to see where it clips
    text_area1.text = text1
    text_area2.text = text2
    text_area3.text = text3
    lenList = 1 + lenList
    print(lenList)
  
    if lenList < 2:
        pos1 = text1.split(", ")
        pos2 = text2.split(", ")
        pos3 = text3.split(", ")
        
        positionAcceList.append([float(pos1[0]),float(pos1[1]),float(pos1[2])])  
        positionGyroList.append([float(pos2[0]),float(pos2[1]),float(pos2[2])])  
        positionMagList.append([float(pos3[0]),float(pos3[1]),float(pos3[2])]) 
        #print(positionList)
    elif lenList == 2:
        acceleration =  Mapping.Mapping(positionAcceList)
        gyro = Mapping.Mapping(positionGyroList)
        mag = Mapping.Mapping(positionMagList)
        #print(acceleration.list)
        #print(gyro.list)
        #print(positionMagList)
        max0 = acceleration.maxPosition()
        max1 = gyro.maxPosition()
        max2 = mag.maxPosition()
        
        # print("accel")
        # print(acceleration.maxPos)
        # print(acceleration.minPos)
        # print("gyro")
        # print(gyro.maxPos)
        # print(gyro.minPos)
        # print("mag")
        # print(mag.maxPos)
        # print(mag.minPos)
        break
  
    text1= " "
    text2= " "
    text3= " "
    #time.sleep(.005)
    text_area1.text = text1
    text_area2.text = text2
    text_area3.text = text3
  

    pass

