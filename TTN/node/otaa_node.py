""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
from network import WLAN
import binascii
import pycom
import socket
import struct
import time
import config as c


#Disable wifi or let default SSID
if c.DIS_WIFI:
    wlan = WLAN()
    wlan.deinit()

# Set heartbeat
pycom.heartbeat(c.HEARTBEAT)

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTA authentication params
dev_eui = binascii.unhexlify(c.DEV_EUI.replace(' ',''))
app_eui = binascii.unhexlify(c.APP_EUI.replace(' ',''))
app_key = binascii.unhexlify(c.APP_KEY.replace(' ',''))

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
lora.add_channel(0, frequency=c.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=c.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=c.LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    if c.DEBUG_CON:
        print('Not joined yet...')
    if c.DEBUG_LED:
        pycom.rgbled(c.RED)
        time.sleep(0.1)
        pycom.rgbled(c.LED_OFF)
        time.sleep(2)

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, c.LORA_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)

i = 0
while True:
    # Prepare the packet
    pkt = c.PKT_PREFIX + bytes([i % 256])
    # Send it
    s.send(pkt)
    if c.DEBUG_CON:
        print('send >> ', pkt)
    if c.DEBUG_LED:
        pycom.rgbled(c.GREEN)
        time.sleep(0.1)
        pycom.rgbled(c.LED_OFF)
    # Wait to receive packet
    time.sleep(4)
    rx = s.recv(256)
    if rx and c.DEBUG_CON:
        pycom.rgbled(c.BLUE)
        time.sleep(0.1)
        pycom.rgbled(c.LED_OFF)
        print("receive << ", rx)
    # Sleep
    time.sleep(c.SLEEP_MAIN)
    i += 1
