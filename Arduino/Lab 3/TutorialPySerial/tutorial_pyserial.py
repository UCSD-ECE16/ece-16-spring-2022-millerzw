import serial #the Pyserial library
import time #for timing purposes

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
    #ser = setup("thingy-ESP32SPP", 115200)
    send_message(ser,"hello world\n")
    time.sleep(3)
    close(ser)
"""
Main entrypoint for the application
"""
if __name__== "__main__":
    main()
