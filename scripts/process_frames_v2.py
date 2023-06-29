import os
import cv2
import numpy as np

def process_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to obtain a binary image
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask with white pixels inside the contours
    mask = np.zeros_like(frame)
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, mask)

    return result

# Example usage
input_folder = r'C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames'  # Path to the folder containing input frames
output_folder = r'C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames\processed'  # Path to the folder for saving processed frames

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process frames in the input folder and save them to the output folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        frame = cv2.imread(input_path)
        processed_frame = process_frame(frame)
        cv2.imwrite(output_path, processed_frame)
