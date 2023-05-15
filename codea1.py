import board
import displayio
import terminalio
import time
import Mapping
import TDKInvenSenses
import DisplayOutputs
from adafruit_display_text import label
import adafruit_displayio_sh1107

import neopixel
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
    print(lenList)
    if lenList < 35:
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
            
            #axcell = (-52.27,11.96)
            #self.b =(0, 800)
        
      
            # min [[-52.27, -78.45, -34.66]]
            # max [[11.96, 21.97, 24.52]]
            # gyro
            # min [[-12.6, -24.75, -43.35]]
            # max [[65.4, 73.95, 49.65]]
            # mag
            # min [[-8.73, -8.73, -8.73]]
            # max [[8.73, 8.73, 8.73]]
            
            xGyro = gyroMap.maprange((-12.6,4.9),float(pos2[0]))
            yGyro = gyroMap.maprange((-24.75,73.95),float(pos2[1]))
            zgyro = gyroMap.maprange((-43.35,49.65),float(pos2[2]))
                
            xmagMap = magMap.maprange((-8.73,8.73),float(pos3[0]))
            ymagMap = magMap.maprange((-8.73,8.73),float(pos3[1]))
            zmagMap = magMap.maprange((-8.73,8.73),float(pos3[2]))
            
            text_area1.text = acell.returnText()
            text_area2.text = gyro.returnText()
            text_area3.text = magnetic.returnText()
            
            # print(acell.returnText())
            # print(gyro.returnText())
            # print(magnetic.returnText())
            #print(positionList)
    elif lenList == 35:
     
        print("positionGyroList")  
        print(positionAcceList)
        print("positionGyroList")
        print(positionGyroList)
        print("positionMagList")
        print(positionMagList)
        break
    
        text1= " "
        text2= " "
        text3= " "
        #time.sleep(.005)
        text_area1.text = text1
        text_area2.text = text2
        text_area3.text = text3
    
    # fader.update()
    # rgb[4] = fader.color
    # rgb[3] = fader.color
    # rgb[2] = fader.color
    # rgb[1] = fader.color
    # rgb[0] = fader.color
    rgb.write()
    # if  xAcell < 100.0:   
    #     rgb[7] = 255  
    #     rgb[6] = 0  
    #     rgb[5] = 0    
    #     rgb[4] = 0
    #     rgb[3] = 0
    #     rgb[2] = 0  
    #     rgb[1] = 0  
    #     rgb[0] = 0 
    #     rgb.write()
        
    # elif   xAcell > 100 and xAcell < 200:   
    #     rgb[7] = 255  
    #     rgb[6] = 255 
    #     rgb[5] = 0    
    #     rgb[4] = 0
    #     rgb[3] = 0
    #     rgb[2] = 0  
    #     rgb[1] = 0  
    #     rgb[0] = 0 
    #     rgb.write()
        
    # elif  xAcell > 200 and xAcell < 300:   
    #     rgb[7] = 255  
    #     rgb[6] = 255 
    #     rgb[5] = 255    
    #     rgb[4] = 0
    #     rgb[3] = 0
    #     rgb[2] = 0  
    #     rgb[1] = 0  
    #     rgb[0] = 0 
    #     rgb.write()

    # elif  xAcell > 400 and xAcell < 500: 
    #     rgb[7] = 255  
    #     rgb[6] = 255 
    #     rgb[5] = 255   
    #     rgb[4] = 255
    #     rgb[3] = 0
    #     rgb[2] = 0  
    #     rgb[1] = 0  
    #     rgb[0] = 0 
    #     rgb.write()

    # elif   xAcell > 600 and xAcell < 700: 
    #     rgb[7] = 255  
    #     rgb[6] = 255  
    #     rgb[5] = 255   
    #     rgb[4] = 255
    #     rgb[3] = 255
    #     rgb[2] = 0  
    #     rgb[1] = 0  
    #     rgb[0] = 0 
    #     rgb[0] = 0
    #     rgb.write()
    
    # elif   xAcell > 600 and xAcell < 700: 
    #     rgb[7] = 255  
    #     rgb[6] = 255  
    #     rgb[5] = 255   
    #     rgb[4] = 255
    #     rgb[3] = 255
    #     rgb[2] = 255 
    #     rgb[1] = 0  
    #     rgb[0] = 0 
    #     rgb[0] = 0
    #     rgb.write()
        
    # if  xGyro < 100.0:  
    #     rgb[15] = 255  
    #     rgb[14] = 0  
    #     rgb[13] = 0    
    #     rgb[12] = 0
    #     rgb[11] = 0
    #     rgb[10] = 0  
    #     rgb[9] = 0  
    #     rgb[8] = 0 
        
    #     rgb.write()
        
    # elif   xGyro > 100 and xGyro < 200:   
    #     rgb[15] = 255  
    #     rgb[14] = 255
    #     rgb[13] = 0    
    #     rgb[12] = 0
    #     rgb[11] = 0
    #     rgb[10] = 0  
    #     rgb[9] = 0  
    #     rgb[8] = 0 
    #     rgb.write()
        
    # elif  xGyro > 200 and xGyro < 300:   
    #     rgb[15] = 255  
    #     rgb[14] = 255  
    #     rgb[13] = 255    
    #     rgb[12] = 0
    #     rgb[11] = 0
    #     rgb[10] = 0  
    #     rgb[9] = 0  
    #     rgb[8] = 0 
    #     rgb.write()

    # elif  xGyro > 400 and xGyro < 500: 
    #     rgb[15] = 255  
    #     rgb[14] = 255  
    #     rgb[13] = 255    
    #     rgb[12] = 255
    #     rgb[11] = 0
    #     rgb[10] = 0  
    #     rgb[9] = 0  
    #     rgb[8] = 0 
    #     rgb.write()

    # elif   xGyro > 600 and xGyro < 700: 
    #     rgb[15] = 255  
    #     rgb[14] = 255  
    #     rgb[13] = 255    
    #     rgb[12] = 255
    #     rgb[11] = 255
    #     rgb[10] = 0  
    #     rgb[9] = 0  
    #     rgb[8] = 0 
    #     rgb.write()
    # elif   xGyro > 700 and xGyro < 800: 
    #     rgb[15] = 255  
    #     rgb[14] = 255  
    #     rgb[13] = 255    
    #     rgb[12] = 255
    #     rgb[11] = 255
    #     rgb[10] = 255  
    #     rgb[9] = 0  
    #     rgb[8] = 0 
    #     rgb.write()
        

    # time.sleep(1)  
    # # rgb[4] = 0
    # # rgb[3] = 0
    # # rgb[2] = 0  
    # # rgb[1] = 0  
    # # rgb[0] = 0
    # # rgb.write()
    # #print(xAcell)   
    # print(xGyro) 
    pass