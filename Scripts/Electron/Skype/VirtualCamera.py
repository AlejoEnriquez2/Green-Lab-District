import os
import keyboard
import time

running = True
startCameraCommand = "ffmpeg -re -i media/output1h.mp4 -map 0:v -f v4l2 /dev/video1"

def start_camera():
    os.system(startCameraCommand)

def on_key_event(event):
    global running
    if event.name == 'q':
        running = False

keyboard.on_release_key('q', on_key_event)

while running:
    start_camera()
    time.sleep(1)

keyboard.unhook_all()
