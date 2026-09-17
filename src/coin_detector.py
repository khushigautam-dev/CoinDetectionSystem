import cv2

# Load image
image = cv2.imread("data/coins1.jpg")

if image is None:
    print("Image could not be loaded.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# Find external contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

count = 0

for contour in contours:

    area = cv2.contourArea(contour)

    # Ignore small objects
    if area > 30000:

        count += 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        cv2.putText(
            image,
            "Coin",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

print("Coins detected:", count)

# Save result
cv2.imwrite("results/detected_coins.jpg", image)

print("Result saved successfully!")