import tkinter as tk
from tkinter import filedialog, messagebox
import cv2


def detect_coins():
    file_path = filedialog.askopenfilename(
        title="Select Coin Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if not file_path:
        return

    image = cv2.imread(file_path)

    if image is None:
        messagebox.showerror("Error", "Could not load image.")
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

    count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

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
        "Coins Detected: " + str(count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imwrite("results/final_result.jpg", image)

    result_label.config(
        text="Coins Detected: " + str(count)
    )

    messagebox.showinfo(
        "Success",
        "Detection completed!\nResult saved in results folder."
    )


# Create window
window = tk.Tk()
window.title("Coin Detection and Counting System")
window.geometry("500x300")

title = tk.Label(
    window,
    text="Coin Detection and Counting System",
    font=("Arial", 18)
)

title.pack(pady=30)

button = tk.Button(
    window,
    text="Select Image & Detect Coins",
    command=detect_coins,
    font=("Arial", 12)
)

button.pack(pady=20)

result_label = tk.Label(
    window,
    text="Coins Detected: -",
    font=("Arial", 14)
)

result_label.pack(pady=20)

window.mainloop()