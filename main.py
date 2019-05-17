#PEDRO LUCAS DE ANDRADE ARRUDA
#17/05/2019







from thingspeak import Channel #Thingspeak stuff

from thingspeak import ThingSpeakAPI, ProtoHTTPS #Thingspeak stuff

import credentials #For the API_KEY

room = "room"
active_channel = room

room_temp = "Temperature"
room_humidity = 'Relative humidity'
room_lum = 'Luminosity'




channels = [Channel(active_channel, credentials.API_KEY, [room_temp,
                                                          room_humidity,
                                                          room_lum])]



thing_speak = ThingSpeakAPI(channels, protocol_class=ProtoHTTPS, log=True)



import dht
import machine

d_pin= dht.DHT11(machine.Pin(5)) #Inialize pin D1 of nodemcu
lum_pin = machine.ADC(0) #Initialize Pin A0

def get_data():
  d_pin.measure()
  lum_voltage = lum_pin.read() * (3.3 / 1024.0)
  returner = {room_temp : d_pin.temperature(),
              room_humidity : d_pin.humidity(),
              room_lum : lum_voltage}
  
  
def send_data():
  data = get_data()
  thing_speak.send(active_channel1, {room_temp: data[room_temp],
                                     room_humidity: data[room_humidity],
                                     room_lum : data[room_lum]})



