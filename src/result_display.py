import cv2

def display_result(image_path, count):
    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded.")
        return

    cv2.putText(
        image,
        "Coins Detected: " + str(count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Coin Detection Result", image)

    print("Result displayed successfully!")
    print("Total coins:", count)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


display_result("results/detected_coins.jpg", 4)