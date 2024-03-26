# HandNeutralNetworksDesktop

# Hand Gesture Control with PyAutoGUI and Mediapipe

This project enables computer mouse control using hand gestures with the MediaPipe and PyAutoGUI libraries. Different hand movements simulate mouse clicks, right clicks, and mouse holding actions.

## Requirements

To run this project, you need the following libraries:

- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## Code Description

This code detects hand movements using the computer's camera and performs various mouse actions based on these movements. The main workflow consists of the following steps:

- Initialize camera input and configure settings for hand detection.
- Retrieve hand detection results and control the mouse based on different finger positions.
- Perform mouse clicks, right clicks, and mouse holding actions based on finger positions.

## Finger Movements and Functions

This project uses hand gestures to control mouse actions based on the positions of individual fingers. Here's a breakdown of each finger movement and its corresponding function:

- **Index Finger (Pointer Finger):** When the index finger is extended and close to the thumb, it simulates a left mouse click.
- **Middle Finger:** Holding the middle finger close to the thumb initiates a mouse hold action. Releasing the finger ends the hold.
- **Ring Finger:** Double-tapping the ring finger near the thumb triggers a double left mouse click.
- **Pinky Finger (Little Finger):** Tapping the pinky finger near the thumb simulates a right mouse click.

## Crickle

Crickle is a term used in this project to describe the action of gently tapping or pressing a finger against the thumb. It's a combination of the words "click" and "circle." The crickle action is used to initiate various mouse click actions based on the finger involved.

By incorporating crickle gestures, this project offers intuitive control over mouse functions using natural hand movements.

## How to Use

1. Clone the project files to your computer.
2. Install the required libraries.
3. Run the code.

## Contribution

This project is open-source and open to contributions. Feel free to open a pull request to contribute.
