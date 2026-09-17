import cv2


def test_image_loading():
    image = cv2.imread("data/coins1.jpg")

    assert image is not None
    print("Test passed: Image loaded successfully.")


def test_image_size():
    image = cv2.imread("data/coins1.jpg")

    assert image.shape[0] > 0
    assert image.shape[1] > 0
    print("Test passed: Image has valid dimensions.")


test_image_loading()
test_image_size()

print("All tests passed successfully!")