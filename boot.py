


# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import uos, machine

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

#import webrepl

#webrepl.start()

gc.collect()

import network
import time
import credentials #For network information

sta_if = network.WLAN(network.STA_IF)
ap_if  = network.WLAN(network.AP_IF)
sta_if.active(True)
ap_if.active(False)
sta_if.connect(credentials.SSID,credentials.PASS)

time.sleep(5)

print(sta_if.ifconfig())




import main as m

button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)


while 1 and button.value() == 1:
  m.send_data()
  time.sleep(120)






