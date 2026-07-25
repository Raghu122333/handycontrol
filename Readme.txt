# 🖐️ Hand Gesture Control using OpenCV & MediaPipe

A real-time computer vision project that recognizes hand gestures using a webcam and controls the computer with predefined actions.

## 🚀 Features

* Detects a single hand in real time using MediaPipe Hands.
* Recognizes multiple hand gestures.
* Executes different keyboard and mouse actions based on the detected gesture.
* Displays the detected gesture on the webcam feed.
* Prevents repeated actions by triggering only when the gesture changes.

## 🛠️ Technologies Used

* Python 3
* OpenCV
* MediaPipe
* PyAutoGUI

## 📂 Project Structure

```text
Hand-Gesture-Control/
│── main.py
│── README.md
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Hand-Gesture-Control.git
cd Hand-Gesture-Control
```

### 2. Install the required packages

```bash
pip install opencv-python mediapipe pyautogui
```

## ▶️ Running the Project

```bash
python main.py
```

Make sure your webcam is connected before running the program.

## ✋ Supported Gestures

| Gesture         | Finger Pattern | Action                            |
| --------------- | -------------- | --------------------------------- |
| ✊ Fist          | `[0,0,0,0,0]`  | Presses **Space**                 |
| 🖐️ Open Palm   | `[1,1,1,1,1]`  | Types **"prasad tech in telugu"** |
| ✌️ Peace        | `[0,1,1,0,0]`  | Presses **Down Arrow**            |
| ☝️ Point        | `[0,1,0,0,0]`  | Moves mouse cursor to the right   |
| 🖖 Four Fingers | `[0,1,1,1,1]`  | Presses **Enter**                 |
| 🤟 OK (custom)  | `[0,0,1,1,1]`  | Scrolls up                        |

> **Note:** The gesture names and finger patterns are based on the logic implemented in the code and may differ from conventional hand signs.

## ⚙️ How It Works

1. Captures live video from the webcam.
2. Converts each frame from BGR to RGB.
3. Detects hand landmarks using MediaPipe Hands.
4. Determines whether each finger is open or closed.
5. Maps the finger pattern to a predefined gesture.
6. Executes the corresponding keyboard or mouse action using PyAutoGUI.
7. Displays the recognized gesture on the video feed.

## 📸 Demo

You can add screenshots or a GIF here.

Example:

```
demo.gif
```

or

```
screenshots/
```

## 🔮 Future Improvements

* Support for both left and right hands.
* More accurate thumb detection.
* Custom gesture training.
* Mouse movement using fingertip tracking.
* Volume and brightness control.
* Gesture-based media player controls.
* Virtual drawing mode.

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Raghu Venkata Reddy**

If you found this project useful, consider giving it a ⭐ on GitHub.
