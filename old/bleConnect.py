import time
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import neopixel
import board
class BleConnect:
    def __init__(self,SEND_RATE):
        
        self.SEND_RATE  = SEND_RATE 
        self.ble = BLERadio()
        self.uart_server = UARTService()
        self.advertisement = ProvideServicesAdvertisement(self.uart_server)
        self.count = 0
        self.last_send = time.monotonic()
    def conect(self):
        print("WAITING1...")
        # Advertise when not connected.
        self.ble.start_advertising( self.advertisement)
        while not  self.ble.connected:
            pass
        # Connected
        self.ble.stop_advertising()
        print("CONNECTED")
        
        self.update()
   
    def update(self):
        # Loop and read packets
        self.rgb1 = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)
        while  self.ble.connected:
            # INCOMING (RX) check for incoming text
            if  self.uart_server.in_waiting:
                raw_bytes =  self.uart_server.read( self.uart_server.in_waiting)
                text = raw_bytes.decode().strip()
               
                # print("raw bytes =", raw_bytes)
                print("RX:", text)
            # OUTGOING (TX) periodically send text
            if time.monotonic() - self.last_send >  self.SEND_RATE:
                text = "COUNT = {}\r\n".format( self.count)
                print("TX:", text.strip())
                self.rgb1[self.count] = (255,255,0)
                self.uart_server.write(text.encode())
                
                if self.count < 31:
                    self.count += 1
                else:
                    self.count    
                self.last_send = time.monotonic()

        # Disconnected
        print("DISCONNECTED")
