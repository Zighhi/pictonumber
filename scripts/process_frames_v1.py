import cv2
import numpy as np
import os

def process_frame(input_path, output_path):
    # Read the input frame
    frame = cv2.imread(input_path)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank image to draw the outlines
    outline = np.zeros_like(frame)

    # Draw the contours on the outline image
    cv2.drawContours(outline, contours, -1, (255, 255, 255), thickness=2)

    # Convert the processed frame to black and white based on the outlines
    processed_frame = cv2.cvtColor(outline, cv2.COLOR_BGR2GRAY)

    # Print the frame being processed
    print("Processing frame:", input_path)

    # Save the processed frame
    cv2.imwrite(output_path, processed_frame)

# Example usage
input_folder = r'C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames'
output_folder = r'C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames\processed'  # Path to the folder for saving processed frames


# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each frame in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        process_frame(input_path, output_path)
