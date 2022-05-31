"""
@author: Ramsin Khoshabeh
"""

from ECE16Lib.Communication import Communication
from time import sleep
import socket, pygame
from time import time

# Setup the Socket connection to the Space Invaders game
host = "127.0.0.1"
port = 65432
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.connect((host, port))
mySocket.setblocking(False)

fileData = open("GameData.txt","r+")

#Variable move speed
#Move and shoot at same time
#Fixed sensitivity but could use more work --> arduino

class PygameController:
    comms = None
    fs = 50
    procTime = 0.1
    ## Changing procTIme will adjust how fast the player can move ()()() later in the lab its important
    timeTable = [0.1, 0.01, 0.005]

    def __init__(self, serial_name, baud_rate):
        self.comms = Communication(serial_name, baud_rate)

    def run(self):
        # 1. make sure data sending is stopped by ending streaming
        self.comms.send_message("stop")
        self.comms.clear()

        # 2. start streaming orientation data
        input("Ready to start? Hit enter to begin.\n")
        self.comms.send_message("start")

        # 3. Forever collect orientation and send to PyGame until user exits
        print("Use <CTRL+C> to exit the program.\n")
        prevTime = time()
        while True:
            message = self.comms.receive_message()
            if (message != None):
                #print(message)
                try:
                    (m1, m2, m3) = message.split(',')
                    # m1= type of move
                    # m2= speed mode
                    # m3= shooting
                except ValueError:  # if corrupted data, skip the sample
                    continue
                command = None
                message = int(m1)
                # if message == 0:
                #   command = "FLAT"
                # if message == 1:
                #   command = "UP"
                if message == 2:
                    command = "FIRE"
                elif message == 3:
                    command = "LEFT"
                elif message == 4:
                    command = "RIGHT"

                self.procTime = self.timeTable[int(m2)]
                self.procTime=1

                currTime = time()
                if command is not None:
                    if (currTime - prevTime > self.procTime):
                        prevTime = currTime
                        mySocket.send(command.encode("UTF-8"))

                        #fileData.seek(0)
                        #msgToArduino = fileData.readline()
                        msgToArduino="ey"
                        if (msgToArduino != "" and msgToArduino != "\n"):
                            self.comms.send_message(msgToArduino)
                            print(msgToArduino)

                        if (int(m3) == 1):
                            commandTwo="FIRE"
                            mySocket.send(commandTwo.encode("UTF-8"))

                try:
                    data = mySocket.recv(1024)
                    data=data.decode("utf-8")
                    print(data)
                    #self.comms.send_message(data)
                except BlockingIOError:
                    continue


                #fileData.seek(0)

                #msgToArduino=fileData.readline()

                ##note last working on the socket in process
                ##send message to socket from main
                ##recieve from socket in controller
                ##send from controller to arduino

                ##double note, try except blocks necessary fro IO erros

if __name__ == "__main__":
    serial_name = "COM4"
    baud_rate = 115200
    controller = PygameController(serial_name, baud_rate)
    try:
        controller.run()
    except(Exception, KeyboardInterrupt) as e:
        print(e)
    finally:
        print("Exiting the program.")
        controller.comms.send_message("stop")
        controller.comms.close()
        mySocket.send("QUIT".encode("UTF-8"))
        mySocket.close()

        fileData.close()

    input("[Press ENTER to finish.]")
