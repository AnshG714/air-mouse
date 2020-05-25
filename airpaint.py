import pyautogui
import time
import serial

time.sleep(10)
distance = 200

"""
NOTE: Uncomment all this stuff when the board has been connected to the
computer. 

try:
    frdm = serial.Serial('/dev/tty.usbmodem1421', 9600)  # replace

except:
    print("failed to connect")
    exit()

"""

# just something that draws a spiral.
pyautogui.click()
while distance > 0:

    pyautogui.dragRel(distance, 0, duration=0.2,
                      button='left')   # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.2,
                      button='left')   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2,
                      button='left')  # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.2,
                      button='left')  # move up


def defunc():
    """
    remove all this from a function.
    """
    while True:
        latestData = frdm.readline()
        delX, delY, buttonPressed = parse(latestData)
        if buttonPressed:
            pyautogui.dragRel(delX, delY, duration=0.1, button='left')
        else:
            pyautogui.moveRel(delX, delY, duration=0.1)


def parse(data: str):
    """
    returns the delta X, delta Y and boolean indicating
    whether the relevant button on the frdm button is pressed or not. 
    """
    dataList = data.split(",")

    deltaX = dataList[1] - dataList[0]
    deltaY = dataList[3] - dataList[2]

    isPressed = dataList[4] == -1

    return deltaX, deltaY, isPressed
