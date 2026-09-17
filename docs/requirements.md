# System Requirements

## 1. Functional Requirements

### FR1 - Image Input
The system shall allow the user to select a coin image from the computer.

### FR2 - Image Preprocessing
The system shall convert the input image into grayscale and apply thresholding to prepare it for coin detection.

### FR3 - Coin Detection
The system shall identify the external contours of visible coins in the image.

### FR4 - Coin Counting
The system shall count the detected coin objects and calculate the total number of coins.

### FR5 - Result Display
The system shall display the detected coins and show the total number of coins detected.

### FR6 - Result Saving
The system shall save the processed image with the detection result in the results folder.

---

## 2. Non-Functional Requirements

### NFR1 - Usability
The system should provide a simple graphical interface so that users can select an image and run the detection easily.

### NFR2 - Performance
The system should process a normal-sized input image within a few seconds on a standard computer.

### NFR3 - Reliability
The system should handle invalid or unreadable image files without crashing.

### NFR4 - Maintainability
The project should be divided into separate modules so that individual components can be modified easily.

### NFR5 - Resource Efficiency
The system should use basic image processing techniques and should not require a large machine-learning model or dataset.

### NFR6 - Portability
The system should be able to run on a computer with Python, OpenCV, and Tkinter installed.

---

## 3. Input

- JPG, JPEG, or PNG image
- Image containing clearly visible coins

## 4. Output

- Total number of detected coins
- Image showing detected coins
- Saved result image in the results folder

## 5. Project Limitations

- The current system is designed for clearly visible and sufficiently separated coins.
- It may not accurately detect heavily overlapping coins.
- The system currently counts coins but does not identify their denominations or monetary values.