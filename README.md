# Coin Detection and Counting System Using Computer Vision

## 1. Project Overview

The Coin Detection and Counting System is a Computer Vision project that detects and counts coins present in an image.

The system uses basic image processing techniques to identify visible coin objects and calculate their total count. The detected result is displayed to the user and saved as an output image.

## 2. Problem Statement

Counting coins manually from an image can be time-consuming and may lead to mistakes.

This project provides a simple automated method to detect and count visible coins using Computer Vision techniques.

## 3. Objectives

- Detect coins from an input image.
- Preprocess the input image.
- Identify coin objects using contours.
- Count the detected coins.
- Display the detection result.
- Save the processed result.
- Provide a simple graphical interface.

## 4. Main Features

- Image selection
- Image preprocessing
- Grayscale conversion
- Thresholding
- Contour detection
- Coin detection
- Automatic coin counting
- Result visualization
- Output image saving
- Graphical user interface

## 5. Technologies Used

- Python
- OpenCV
- NumPy
- Tkinter
- Visual Studio Code

## 6. Project Modules

### Image Input Module

Loads the selected image into the system.

### Image Preprocessing Module

Converts the input image into grayscale and applies thresholding to prepare it for detection.

### Coin Detection Module

Uses external contours to identify visible coin objects.

### Coin Counting Module

Counts the detected coin objects and provides the total number of coins.

### Result Display Module

Displays the detected result and total number of coins.

### GUI Module

Provides a simple interface for selecting an image and running the detection process.

## 7. Working Process

```text
Input Image
     ↓
Image Preprocessing
     ↓
Grayscale Conversion
     ↓
Thresholding
     ↓
Contour Detection
     ↓
Coin Detection
     ↓
Coin Counting
     ↓
Result Display
     ↓
Save Result