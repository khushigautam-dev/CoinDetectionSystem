# System Architecture

## 1. Architecture Overview

The Coin Detection and Counting System follows a simple modular architecture. The system takes a coin image as input, processes the image using Computer Vision techniques, detects the coins, counts them, and displays the result.

## 2. Architecture Components

### 1. User Interface
The user selects a coin image through the graphical user interface.

### 2. Image Input Module
The selected image is loaded using OpenCV.

### 3. Image Preprocessing Module
The image is converted from RGB/BGR format to grayscale. Thresholding is then applied to separate the coins from the background.

### 4. Coin Detection Module
External contours are detected from the thresholded image. Large contours are considered as coin objects.

### 5. Coin Counting Module
The detected coin objects are counted to obtain the total number of coins.

### 6. Result Display Module
The total number of detected coins is displayed to the user. Bounding boxes are also drawn around detected coins.

### 7. Output Module
The processed image is saved in the `results` folder.

## 3. System Workflow

```text
User
  ↓
Select Coin Image
  ↓
Image Input
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
Display Result
  ↓
Save Output Image