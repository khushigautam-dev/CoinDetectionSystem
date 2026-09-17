# Testing Documentation

## 1. Testing Objective

The purpose of testing is to verify that the Coin Detection and Counting System works correctly and produces the expected results.

## 2. Test Environment

- Operating System: Windows
- Programming Language: Python
- Computer Vision Library: OpenCV
- GUI Library: Tkinter
- Development Environment: Visual Studio Code

## 3. Test Cases

| Test Case | Input | Expected Result | Status |
|---|---|---|---|
| TC01 | Valid coin image | Image loads successfully | Pass |
| TC02 | Valid coin image | Image dimensions are valid | Pass |
| TC03 | Image containing 4 coins | System detects 4 coins | Pass |
| TC04 | Valid image | Detection result is displayed | Pass |
| TC05 | Valid image | Result image is saved | Pass |
| TC06 | Invalid/unreadable image | Error message is displayed | Pass |

## 4. Unit Testing

The project contains a test file:

`tests/test_coin_detection.py`

The test checks whether:

- The input image can be loaded.
- The image has valid dimensions.

Both tests were executed successfully.

## 5. Functional Testing

The complete system was tested using a sample image containing four coins.

### Expected Output

```text
Coins detected: 4