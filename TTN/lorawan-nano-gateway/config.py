""" LoPy LoRaWAN Nano Gateway configuration options """

GATEWAY_ID = '<gateway_eui>'

WIFI_SSID = '<ssid>'
WIFI_PASS = '<password>'

SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

LORA_FREQUENCY = 868100000
LORA_DR = "SF7BW125"   # DR_5

# Debug
DEBUG_LED = True
DEBUG_CON = True

# LED color
LED_OFF = 0x000000
GREEN = 0x007f00
YELLOW = 0x7f7f00
RED = 0x7f0000
BLUE = 0x00007f
