

# Hand Gesture Control

This project is a hand gesture control system using OpenCV, MediaPipe, and various other libraries. It uses hand landmarks to control screen brightness and volume based on hand gestures detected from the webcam feed.

## Requirements

- Python 3.x
- `opencv-python` library
- `mediapipe` library
- `numpy` library
- `pyautogui` library
- `screen-brightness-control` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
    ```bash
    pip install opencv-python mediapipe numpy pyautogui screen-brightness-control
    ```

## Usage

1. Run the script:
    ```bash
    python script_name.py
    ```
2. The webcam feed will start, and you can use hand gestures to control the brightness and volume.

## Hand Gestures

### Left Hand
- **Brightness Control**: 
  - Distance between the thumb tip and index finger tip controls the brightness.
  - The closer the thumb and index finger, the lower the brightness. The further apart, the higher the brightness.

### Right Hand
- **Volume Control**:
  - If the thumb tip is above the index finger tip, the volume will increase.
  - If the thumb tip is below the index finger tip, the volume will decrease.

## Notes

- Ensure your webcam is working properly.
- Adjust the distance range `[15, 220]` and brightness range `[0, 100]` based on your setup if needed.
- The hand gesture detection might not be perfect and can sometimes result in errors.

## License

This project is licensed under the MIT License.
