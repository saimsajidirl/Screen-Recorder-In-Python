import cv2
import numpy as np
import pyautogui
import time
import sounddevice as sd
import soundfile as sf
import pyaudio
import keyboard  # Make sure to install it: pip install keyboard
import threading
import pygetwindow as gw


def print_window_titles():
    windows = gw.getAllTitles()
    for i, title in enumerate(windows):
        print(f"{i + 1}. {title}")
    return windows

selected_index = int(input("Enter the index of the window you want to record: ")) - 1

try:
    window_title = print_window_titles()[selected_index]
except IndexError:
    print("Invalid index. Exiting.")
    exit()

window = gw.getWindowsWithTitle(window_title)

if not window:
    print(f"No window found with title '{window_title}'. Exiting.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_video = cv2.VideoWriter("Screenrecorded_with_internal_audio.mp4", fourcc, 20.0, (1920, 1080))

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

duration_seconds = 60
start_time = time.time()
end_time = start_time + duration_seconds
print("Video recording started.")

audio_filename = "internal_audio.wav"
sd.default.samplerate = RATE

def record_audio():
    with sf.SoundFile(audio_filename, mode='x', samplerate=RATE, channels=CHANNELS, subtype='PCM_16') as audio_file:
        while True:
            audio_data = sd.rec(CHUNK, channels=CHANNELS, dtype='int16')
            sd.wait()
            audio_file.write(audio_data)
            
            if keyboard.is_pressed('F12'):
                break

# Start recording audio in a separate thread
audio_thread = threading.Thread(target=record_audio)
audio_thread.start()

while True:
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output_video.write(frame)

    current_time = time.time()
    if current_time > end_time or keyboard.is_pressed('F12'):
        break

# Wait for the audio recording thread to finish
audio_thread.join()

output_video.release()
print("Video recorded with internal audio.")
