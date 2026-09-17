import cv2

from coin_counter import count_coins


def detect_coins(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        gray, 220, 255, cv2.THRESH_BINARY_INV
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 30000:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

    count = count_coins(image_path)

    cv2.putText(
        image,
        "Coins Detected: " + str(count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imwrite("results/final_result.jpg", image)

    print("================================")
    print("COIN DETECTION SYSTEM")
    print("================================")
    print("Total coins detected:", count)
    print("Final result saved successfully!")


image_path = "data/coins1.jpg"

detect_coins(image_path)