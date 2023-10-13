import os
import keyboard
import time

running = True

startVirtualCamera = "sudo modprobe v4l2loopback devices=1 video_nr=1 card_label='VirtualWebCam'"
os.system(startVirtualCamera)
time.sleep(3)

videoCommand = "ffmpeg -re -i media/output1h.mp4 -map 0:v -f v4l2 /dev/video1"

def start_camera():    
    os.system(videoCommand)

def on_key_event(event):
    global running
    if event.name == 'q':
        running = False

keyboard.on_release_key('q', on_key_event)

while running:
    start_camera()
    time.sleep(1)

keyboard.unhook_all()
