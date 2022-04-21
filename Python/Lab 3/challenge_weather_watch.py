from pyowm import OWM
from datetime import date

import serial #the Pyserial library
import time #for timing purposes

owm=OWM('fcc8e8f6ccdb6b424c31379ad974fb22').weather_manager()
weather=owm.weather_at_place('San Diego,CA,US').weather
#print(weather.temperature('fahrenheit'))


def setup(serial_name,baud_rate):
    ser=serial.Serial(serial_name,baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()

def send_message(ser, message):
   if(message[-1] != '\n'):
       message = message + '\n'
   ser.write(message.encode('utf-8'))

def main():
    ser=setup("COM4",115200)
    #send_message(ser, stringToArduino)
    #time.sleep(1)
    #close(ser)

if __name__=="__main__":
    main()


ser=setup("COM4",115200)
while True:
    # watch needs Time
    # Date
    # Weather: Cloudy/Sunny + temp
    temp = str(weather.temperature('fahrenheit')).partition(",")[0]  # first part of the temp string: current Temp
    temp = temp[1:]
    currWeather = "{0:<15}".format(str(weather.detailed_status)) + " " + temp  # add clpudy/sunny and temp string

    t = time.localtime()  # get the local time on the machine
    currentTime = time.strftime("%H:%M:%S", t)

    currentDate = str(date.today())  # get current date

    stringToArduino = currentDate + "," + currentTime + "," + currWeather  # add the strings together

    send_message(ser, stringToArduino) # send the string to arduino using , as delimiter
    time.sleep(1) # wait 1 second



