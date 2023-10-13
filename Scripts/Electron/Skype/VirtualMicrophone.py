import os
import keyboard
import time

running = True

# Define your ffmpeg command for audio input
startAudioCommand = "ffmpeg -re -i media/audio.mp3 -f s16le -acodec pcm_s16le -ac 2 -ar 44100 - | ffmpeg -f s16le -acodec pcm_s16le -ac 2 -ar 44100 -i - -f alsa default"

def start_audio():
    os.system(startAudioCommand)

def on_key_event(event):
    global running
    if event.name == 'q':
        running = False

keyboard.on_release_key('q', on_key_event)

while running:
    start_audio()
    time.sleep(1)  # Adjust the sleep duration as needed

keyboard.unhook_all()
