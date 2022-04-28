from ECE16Lib.IdleDetector import IdleDetector
import time

if __name__ == "__main__":
    idleDetect = IdleDetector("COM4",115200)
    print(idleDetect)

if __name__ == "__main__":
  try:
    # Main program code should go here
    idleDetect= IdleDetector("COM4",115200)
    idleDetect.startComms()
    print("Normal program execution finished")
  except KeyboardInterrupt:
    print("User stopped the program with CTRL+C input")
  finally:
    # Clean up code should go here (e.g., closing comms)
    print("Cleaning up and exiting the program")
