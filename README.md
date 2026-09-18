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

## 8. Project Structure

```text
CoinDetectionSystem
│
├── data
│   └── coins1.jpg
│
├── docs
│   ├── requirements.md
│   ├── architecture.md
│   ├── testing.md
│   ├── use_case_diagram.md
│   ├── class_diagram.md
│   ├── sequence_diagram.md
│   └── methodology.md
│
├── results
│   ├── detected_coins.jpg
│   └── final_result.jpg
│
├── src
│   ├── app.py
│   ├── coin_counter.py
│   ├── coin_detector.py
│   ├── main.py
│   ├── result_display.py
│   └── test_image.py
│
├── tests
│   └── test_coin_detection.py
│
├── README.md
├── statement.md
└── venv

9. Installation
Step 1: Create Virtual Environment
python -m venv venv
Step 2: Activate Virtual Environment

On Windows:

venv\Scripts\activate
Step 3: Install Required Libraries
python -m pip install opencv-python numpy pillow

Tkinter is used for the graphical interface and is normally included with the standard Python installation on Windows.

10. How to Run
Run the Graphical Interface

From the project root folder:

cd src
python app.py

A window will open. Select a coin image and click Select Image & Detect Coins.

The detected coin count will be displayed and the result will be saved in the results folder.

Run the Main Program
From the project root folder:

python src/main.py

The program will detect the coins and save the final result.

Run the Tests

From the project root folder:

python tests/test_coin_detection.py

Expected output:

Test passed: Image loaded successfully.
Test passed: Image has valid dimensions.
All tests passed successfully!
11. Testing

The system was tested using a sample image containing four visible coins.

Expected result:

Coins detected: 4

Actual result:

Coins detected: 4

The image loading and image dimension tests also passed successfully.

12. Dataset and Methodology

This project does not use a machine-learning dataset or a trained machine-learning model.

The project uses traditional Computer Vision and image-processing techniques.

The main processing steps are:

Load the input image.
Convert the image to grayscale.
Apply thresholding.
Detect external contours.
Filter contours based on area.
Count the detected coin objects.
Draw bounding boxes around detected coins.
Save the final result.

A sample coin image is used for functional testing.

13. Limitations
The current system works best with clearly visible coins.
Coins should be sufficiently separated from each other.
Heavily overlapping coins may not be detected correctly.
The system currently counts coins but does not identify their denominations.
The system does not calculate the total monetary value of the coins.
14. Future Enhancements
Detect different coin denominations.
Calculate the total monetary value.
Support multiple input images.
Improve detection of overlapping coins.
Add live camera-based detection.
Improve detection for different backgrounds.
Explore machine-learning-based object detection in future versions.
15. Conclusion

The Coin Detection and Counting System demonstrates the use of basic Computer Vision techniques for automatic object detection and counting.

The project applies image preprocessing, thresholding, contour detection, and object counting to detect visible coins from an image.

The system provides a simple graphical interface, displays the detected coin count, and saves the processed result for future reference.