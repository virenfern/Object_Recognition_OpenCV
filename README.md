Mouse Control using OpenCV
Description

This project uses OpenCV and Python to detect motion from a webcam. The program captures video, detects moving objects using background subtraction, and draws a rectangle around the detected movement. This idea can be extended to control the mouse using hand gestures.

Requirements

Python

OpenCV

NumPy

Install the required libraries:

pip install opencv-python numpy
How it Works

The program captures video from the webcam.

Background subtraction is applied to detect movement.

Contours of moving objects are found.

Small movements are ignored.

A green rectangle is drawn around detected objects.

The processed video is displayed on the screen.

Press q to exit the program.

Output

The webcam window shows detected moving objects highlighted with green rectangles.
