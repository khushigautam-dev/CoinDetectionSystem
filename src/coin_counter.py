import cv2

def count_coins(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        gray, 220, 255, cv2.THRESH_BINARY_INV
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 30000:
            count += 1

    return count


# Test the module
image_path = "data/coins1.jpg"

total = count_coins(image_path)

print("Total coins:", total)