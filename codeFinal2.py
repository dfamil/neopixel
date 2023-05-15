import board
import displayio
import terminalio
import time
import Mapping
import TDKInvenSenses
import DisplayOutputs
from adafruit_display_text import label
import adafruit_displayio_sh1107

import adafruit_fancyled.adafruit_fancyled as fancy
from fader_color.fader import Fader
import fancy.fancyCRGB as crgbColors
from fader_color.gradent import Gradent
import Dict2Class as dict
from fader_color.colors import pride, halloween, ireland

BRIGHTNESS=.04
rgb = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)
gradients = Gradent([
    crgbColors.RED, crgbColors.ORANGE, crgbColors.YELLOW, crgbColors.GREEN, crgbColors.BLUE, crgbColors.VIOLET
],True,40,.04)
newGradient= gradients.create_gradient()
#print(color_rgb.palette_names[1])

pride = (6684672, 6684672, 6684672, 6684928, 6685184, 6685696, 6686208, 6687232, 6688256, 6689792, 6691584, 6693632, 6695936, 6698752, 6701824, 6705408, 6709248, 5334528, 3630592, 2319872, 1336832, 681472, 288256, 91648, 26112, 22016, 15105, 9732, 5642, 2836, 1059, 311, 81, 102, 102, 102, 65638, 196710, 393318, 655462, 917606, 1310816, 1704003, 2228268, 2752539, 3342350, 4063238, 4849666, 5701632, 6684672)

fader = Fader(newGradient)
i=0
previous = None


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

        (a1, a2), (b1, b2) =  (-52.27,11.96),(0, 800)
        return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

#print("%g maps to %g" % (-2.27, maprange(-2.27)))
maprange(-2.27)
accelerationMap =  Mapping.Mapping()
gyroMap = Mapping.Mapping()
magMap = Mapping.Mapping()
while True:
    lenList = 1 + lenList
    if lenList < 5:
            acellText = acell.update("acceleration")
            gyroText =gyro.update("gyro")
            magneticText = magnetic.update("magnetic")
            pos1 = acell.returnText().split(", ")
            pos2 = gyro.returnText().split(", ")
            pos3 = magnetic.returnText().split(", ")
            xAcell = accelerationMap.maprange(float(pos1[0]))
            yAcell = accelerationMap.maprange(float(pos1[1]))
            zAcell = accelerationMap.maprange(float(pos1[2]))

            xGyro = gyroMap.maprange(float(pos1[0]))
            yGyro = gyroMap.maprange(float(pos1[1]))
            zgyro = gyroMap.maprange(float(pos1[2]))

            xmagMap = magMap.maprange(float(pos1[0]))
            ymagMap = magMap.maprange(float(pos1[1]))
            zmagMap = magMap.maprange(float(pos1[2]))

            text_area1.text = acell.returnText()
            text_area2.text = gyro.returnText()
            text_area3.text = magnetic.returnText()

            # print(acell.returnText())
            # print(gyro.returnText())
            # print(magnetic.returnText())
            #print(positionList)
    elif lenList == 5:
        break

        text1= " "
        text2= " "
        text3= " "
        #time.sleep(.005)
        text_area1.text = text1
        text_area2.text = text2
        text_area3.text = text3

    fader.update()
    if fader.color != previous:

        rgb[i] = fader.color

        rgb.write()
        previous = fader.color
    time.sleep(0.2)
    if i < 31:
        rgb[i] = 0
        i = 1+i
    else:
        rgb[i] = 0
        i=0

    pass
