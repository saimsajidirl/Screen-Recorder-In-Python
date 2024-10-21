# Screen-Recorder-In-Python

Documentation for Screen Recording with Internal Audio

This Python script records the screen along with internal audio (from your computer) for a specified duration. The program allows the user to select a window by its title for recording, and it saves the video and audio as a .mp4 and .wav file, respectively.
Prerequisites:

To run this script, you need to have the following libraries installed:

    cv2 (OpenCV for screen recording and video processing)
    numpy (for array manipulations)
    pyautogui (for taking screenshots)
    sounddevice (for capturing internal audio)
    soundfile (for saving audio data to a .wav file)
    pyaudio (for managing audio streams)
    keyboard (for handling keypresses)
    pygetwindow (for listing and interacting with open windows)

Make sure to install the required libraries using pip:

bash

pip install opencv-python numpy pyautogui sounddevice soundfile pyaudio keyboard pygetwindow

Overview of Script Components:

    Window Selection:
        The script lists all currently open windows.
        You can select a window by its title, which will then be the area recorded by the script.

    Video Recording:
        The screen within the selected window is captured using screenshots (pyautogui.screenshot()) in real time.
        These screenshots are saved as frames in a video file (cv2.VideoWriter).

    Audio Recording:
        The script records the internal audio using the sounddevice library, saving it in real-time to a .wav file.
        The audio is recorded in a separate thread so that it doesn't block the video recording process.

    Stopping the Recording:
        You can stop both video and audio recording by pressing the F12 key.

Detailed Walkthrough:

    Window Titles Listing:
        The function print_window_titles() retrieves all currently open window titles using pygetwindow.getAllTitles(). This list is displayed, and the user can select one by providing the index.
        If an invalid index is entered, the script exits.

    Video Recording Setup:
        The video capture settings are configured using OpenCV's cv2.VideoWriter. The video is encoded using the XVID codec with a frame rate of 20 frames per second, and the video resolution is set to 1920x1080 (HD).

    Audio Recording Setup:
        The audio is recorded in a separate thread using sounddevice.rec() which captures chunks of audio in real time. These chunks are written to a .wav file.
        The audio recording continues in a loop until the F12 key is pressed.

    Main Recording Loop:
        The pyautogui.screenshot() function is used to capture the content of the selected window in real-time. This screenshot is then converted to a format suitable for OpenCV and written to the video file.
        The loop continues until the specified duration (60 seconds in this case) is reached or F12 is pressed.

    Stopping the Recording:
        Pressing the F12 key stops both the audio and video recording. The audio thread is joined to ensure it finishes before the script exits.

    Final Cleanup:
        The video file is closed using output_video.release(), and a confirmation message is printed.
