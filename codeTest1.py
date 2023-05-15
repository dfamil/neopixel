import board
import displayio
import terminalio
import neopixel
import time
import Mapping
import TDKInvenSenses
import DisplayOutputs
from adafruit_display_text import label
import adafruit_displayio_sh1107
# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2
displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

# Make the display context
splash = displayio.Group()
display.show(splash)

text1="text1"
text2="text2"
text3="text3"

positionAcceList = []
positionGyroList = []
positionMagList = []

text_area1 = label.Label(terminalio.FONT, text=str(text1),  scale=1, color=0xFFFFFF, x=8, y=8)
splash.append(text_area1)

text_area2 = label.Label(terminalio.FONT, text=str(text2),  scale=1, color=0xFFFFFF, x=8, y=25)
splash.append(text_area2)

text_area3 = label.Label(terminalio.FONT, text=str(text3),  scale=1, color=0xFFFFFF, x=8, y=43)
splash.append(text_area3)
# acellOutputText = DisplayOutputs.DisplayOutputs()
# magneticOutputText = DisplayOutputs.DisplayOutputs()
# gyroOutputText = DisplayOutputs.DisplayOutputs()
acell = TDKInvenSenses.TDKInvenSenses()
gyro = TDKInvenSenses.TDKInvenSenses()
magnetic = TDKInvenSenses.TDKInvenSenses()
acellText = acell.update("acceleration")
gyroText =gyro.update("gyro")
magneticText = magnetic.update("magnetic")
# print(acell.returnText())
# print(gyro.returnText())
# print(magnetic.returnText())
# acellOutputText = acell.returnText()
# gyroOutputText = gyro.returnText()
# magneticOutputText=  magnetic.returnText()

# acellOutputText.outputText(acell.returnText())
# gyroOutputText.outputText(gyro.returnText())
# magneticOutputText.outputText(magnetic.returnText())

# acellOutputText = acell.returnText().update("acceleration")
# gyroOutputText =gyro.returnText().update("gyro")
# magneticOutputText = magnetic.returnText().update("magnetic")
lenList = 0

def maprange(s):
 
        (a1, a2), (b1, b2) = 0, 800
        #return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
    
#print("%g maps to %g" % (-2.27, maprange(-2.27)))
maprange(-2.27)
while True:  
    lenList = 1 + lenList
    if lenList < 5:
            acellText = acell.update("acceleration")
            gyroText =gyro.update("gyro")
            magneticText = magnetic.update("magnetic") 
            pos1 = acell.returnText().split(", ")
            pos2 = gyro.returnText().split(", ")
            pos3 = magnetic.returnText().split(", ")
            positionAcceList.append([float(pos1[0]),float(pos1[1]),float(pos1[2])])  
            positionGyroList.append([float(pos2[0]),float(pos2[1]),float(pos2[2])])  
            positionMagList.append([float(pos3[0]),float(pos3[1]),float(pos3[2])]) 
            text_area1.text = acell.returnText()
            text_area2.text = gyro.returnText()
            text_area3.text = magnetic.returnText()
            # print(acell.returnText())
            # print(gyro.returnText())
            # print(magnetic.returnText())
            #print(positionList)
    elif lenList == 5:
        print(positionAcceList)
        print(positionGyroList)
        print(positionMagList)
        acceleration =  Mapping.Mapping(positionAcceList)
        gyro = Mapping.Mapping(positionGyroList)
        mag = Mapping.Mapping(positionMagList)
        # print(acceleration.list)
        # print(gyro.list)
        # print(positionMagList)
        max0 = acceleration.maxPosition()
        max1 = gyro.maxPosition()
        max2 = mag.maxPosition()
        
        # print("accel")
        # print(acceleration.minPos[0][0])
        # print(acceleration.maxPos[0][0])
        # print(maprange((-7.97)))
        # #print(acceleration.minPos[0][0])
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