Motion Detection using OpenCV

This project uses Python and OpenCV to detect motion from a webcam. The program captures live video, identifies moving objects using background subtraction, and draws a green rectangle around the detected motion.

Libraries Used:
OpenCV (cv2)
NumPy

Install the required libraries using: pip install opencv-python numpy
How the Code Works
Capture Video
The webcam is accessed using cv.VideoCapture(0).

Background Subtraction
The createBackgroundSubtractorMOG2() function separates moving objects from the background.

Frame Processing
Each frame from the webcam is read and converted to grayscale.

Contour Detection
The program finds contours from the foreground mask to detect moving regions.

Noise Removal
Small movements are ignored by checking if the contour area is greater than 1888.

Draw Rectangle
A green rectangle is drawn around the detected moving object.

Display Output
The processed video is shown in a window called Detected Objects.

Exit Program
Press q to close the application.

OpenCV Drawing Parameters
img – Image where shapes are drawn
color – Color in BGR format (example: (0,255,0) for green)
thickness – Thickness of the shape border
lineType – Type of line (default is 8-connected, cv.LINE_AA gives smoother lines)

Output
The webcam window shows moving objects detected and highlighted with green rectangles.
