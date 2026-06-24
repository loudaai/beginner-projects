# Gesture-Controlled Meme Machine

A beginner-friendly Python app that uses OpenCV and MediaPipe Hands to control a local meme video with hand gestures.

## Gestures

- Closed fist: starts the meme video.
- Open palm: stops the meme video.
- Esc key: exits the app.

## Requirements

- Windows
- Python 3.11
- Webcam
- A virtual environment
- OpenCV
- MediaPipe

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install opencv-python mediapipe
```

## Run

Make sure `scubacat.mp4` is in the same folder as `project-8.py`, then run:

```powershell
python project-8.py
```

## Notes

The app uses `cv2.CAP_DSHOW` for webcam access on Windows. If the camera does not open, close other apps that may be using the webcam and try again.
