import pyautogui
import time
import csv

class Coordinate:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

clickStartSkype = "csv/skypeStartMeeting.csv"
clickStopSkype = Coordinate(1072, 1054)
clickMic = Coordinate(929,1051)
clickCamera = Coordinate(989,1049)
clickScreenSharing = "csv/skypeScreenSharing.csv"


startMeetingCoordinates = []
shareScreenCoordinates = []

with open(clickStartSkype, mode='r') as file:
    clickStartSkype = csv.reader(file)
    for row in clickStartSkype:
        startMeetingCoordinates.append(Coordinate(int(row[0]), int(row[1])))

with open(clickScreenSharing, mode='r') as file:
    clickScreenSharing = csv.reader(file)
    for row in clickScreenSharing:
        shareScreenCoordinates.append(Coordinate(int(row[0]), int(row[1])))

def skypeClick(x,y,t):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(t)

def startMeeting(): 
    for i in startMeetingCoordinates:        
        skypeClick(i.X, i.Y, 3) 

def shareScreen():
    for i in shareScreenCoordinates:
        skypeClick(i.X, i.Y, 3)

def micClick():
    skypeClick(clickMic.X, clickMic.Y, 0)

def cameraClick():
    skypeClick(clickCamera.X, clickCamera.Y, 0)

def stopMeeting():
    skypeClick(clickStopSkype.X, clickStopSkype.Y, 0)


def skype():  
    # Start meeting
    startMeeting()
    time.sleep(5)

    #Share screen
    shareScreen()
    time.sleep(3)

    #Turn OFF MIC
    micClick()
    time.sleep(3)

    #Turn ON CAMERA
    cameraClick()
    time.sleep(10)

    # Stop meeting
    stopMeeting()     

skype()



