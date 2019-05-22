



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
import credentials
import not_main as m
import os

sta_if = network.WLAN(network.STA_IF)
ap_if  = network.WLAN(network.AP_IF)
sta_if.active(True)
ap_if.active(False)
sta_if.connect(credentials.SSID,credentials.PASS)

#Delay to wait moden conection
time.sleep(5)

print(sta_if.ifconfig())






#Button to break the main loop
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)



#The main loop
while 1 and button.value() == 1:
  gc.collect()
  result = m.send_data()
  if result is not '0':
    error_file = open('error.txt','a+')
    error_file.write(result+'\n')
    result.close()
    time.sleep(30)
  else:
    time.sleep(120)





