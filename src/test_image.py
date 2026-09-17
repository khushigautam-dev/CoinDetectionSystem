import cv2

image = cv2.imread("data/coins1.jpg")

if image is not None:
    print("Image loaded successfully!")
    print("Image size:", image.shape)
else:
    print("Image could not be loaded.")