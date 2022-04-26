from ECE16Lib.Communication import Communication
import time

if __name__ == "__main__":
    comms = Communication()
    print(comms)




if __name__ == "__main__":
  try:
    # Main program code should go here
    comms = Communication("COM4", 115200)
    comms.clear()
    for i in range(30):
        t = time.localtime(time.time())
        currSeconds = t.tm_sec
        comms.sendMessage(str(currSeconds))
        time.sleep(1)
        print(comms.receive_message())
    print("Normal program execution finished")
  except KeyboardInterrupt:
    print("User stopped the program with CTRL+C input")
  finally:
    # Clean up code should go here (e.g., closing comms)
    print("Cleaning up and exiting the program")


