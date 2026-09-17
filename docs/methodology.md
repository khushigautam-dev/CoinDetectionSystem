# Methodology

## 1. Input

The system takes a digital image containing clearly visible coins.

## 2. Image Preprocessing

The input image is converted into grayscale to simplify image processing.

Thresholding is then applied to separate the foreground objects from the background.

## 3. Coin Detection

The system uses external contour detection to identify the boundaries of objects in the processed image.

Contours with an area greater than the selected minimum area are considered coin objects.

## 4. Coin Counting

Each detected coin object is counted, and the total number of detected coins is calculated.

## 5. Result Visualization

A bounding rectangle is drawn around each detected coin. The total number of detected coins is also displayed on the result image.

## 6. Evaluation Method

The system is evaluated by comparing the detected coin count with the actual number of visible coins in the test image.

For the current test image:

- Actual number of coins: 4
- Detected number of coins: 4
- Detection result: Correct

## 7. Limitations

The current method works best when coins are clearly visible and sufficiently separated. Performance may decrease when coins overlap heavily or when the background has objects similar to coins.