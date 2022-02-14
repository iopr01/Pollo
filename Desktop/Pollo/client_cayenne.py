#!/usr/bin/env python

#import PID
#import sensor_nivelabajo
#import example
#import sensor_nivelarriba
from multiprocessing.connection import Client
from pollo_ecxel import create_load_workbook
import cayenne.client
from datetime import datetime
import time
import ast


# def send_on():
#   client.virtualWrite(3, 1) #Publish "1" to Cayenne MQTT Broker Channel 3
#   print("Button pressed\n")

# def send_off():
#   client.virtualWrite(3, 0) #Publish "0" to Cayenne MQTT Broker Channel 3
#   print("Button released\n")

def on_message(message):
  print("message received: " + str(message))
  msg_list = ast.literal_eval(str(message))
  msg_value = int(msg_list['value'])
  msg_channel = int(msg_list['channel'])

  if msg_value == 1 and msg_channel == 1:
    pass #jalar datos


if __name__ == '__main__':

  # Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
  MQTT_USERNAME  = "ef58da40-8376-11ec-9f5b-45181495093e"
  MQTT_PASSWORD  = "e9d4ea879de75a1b8ed09737a0b2f0a7f37a059c"
  MQTT_CLIENT_ID = "f2c74d10-8376-11ec-8c44-371df593ba58"
  
  client = cayenne.client.CayenneMQTTClient()
  client.on_message = on_message #When message recieved from Cayenne run on_message function
  client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

  date_time = datetime.fromtimestamp(time.time())
  date_time = str(date_time).replace(':', '-').split('.')[0]
  file = f'/home/partenio/Desktop/Pollo/hx711py/Excel/{date_time}.xlsx'
  
  # creating the sheet.
  wb, sheet = create_load_workbook(file)
  blank_row = 3

  value_temp = 0
  value_hum = 0
  value_tanque = 0
  value_peso = 0
  value_comida = 0

  while True:
    client.loop()

    # value_temp, value_hum = PID.funcion1()
    # value_tanque = sensor_nivelabajo.funcion2()
    # value_peso = example.funcion3()
    # value_comida =  sensor_nivelarriba.funcion4()

    client.celsiusWrite(1, value_temp)
    time.sleep(1)

    client.virtualWrite(2, value_hum)
    time.sleep(1)

    client.virtualWrite(3, value_tanque)
    time.sleep(1)

    client.virtualWrite(4, value_peso)
    time.sleep(1)

    client.virtualWrite(5, value_comida)
    time.sleep(1)
    
    value_temp = 1
    value_hum = 2
    value_tanque = 3
    value_peso = 4
    value_comida = 5

    lista = [value_temp, value_hum, value_tanque, value_peso, value_comida]

    time_date = [datetime.fromtimestamp(time.time())]
    # Exel write data
    data = lista + time_date
    sheet.cell(blank_row, 1).value = blank_row - 2
    for i, dat in enumerate(data):
        sheet.cell(blank_row, i + 2).value = dat
    #adjusted_width = (len (time_date) + 2) * 1.2
    #sheet.column_dimensions['17'].width = int(adjusted_width)
    wb.save(file)
    blank_row += 1