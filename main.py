
from thingspeak import Channel #Thingspeak stuff

from thingspeak import ThingSpeakAPI, ProtoHTTPS #Thingspeak stuff

import credentials #For the API_KEY

room = 'room'
active_channel = room

room_temp = 'Temperature'
room_humidity = 'RelativeHumidity'
room_lum = 'Luminosity'




channels = [Channel(active_channel, credentials.API_KEY, [room_temp,room_humidity,room_lum])]



thing_speak = ThingSpeakAPI(channels, protocol_class=ProtoHTTPS, log=True)



import dht
import machine

d_pin= dht.DHT11(machine.Pin(5))#Inialize pin D1 of nodemcu
lum_pin = machine.ADC(0)

def get_data():
  d_pin.measure()
  lum_voltage = lum_pin.read() * (3.3 / 1024.0)
  returner = [d_pin.temperature(),d_pin.humidity(),lum_voltage]
  return returner
  
  
def send_data():
  try:
    data = get_data()
    thing_speak.send(active_channel, {room_temp:data[0],room_humidity:data[1],room_lum:data[2]})
    return '0'
  except exception:
    return (exception)
    



