import os
import cv2
import numpy as np
from PIL import Image

# Specify the folder path containing the JPG files
input_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\screenshots"

# Specify the output MP4 file path
output_file = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\video.mp4"

# Specify the desired duration of the MP4 (in seconds)
duration = 6.02

# Get the list of JPG files in the folder
jpg_files = [file for file in os.listdir(input_folder) if file.endswith(".jpg")]

# Define a sorting function to handle alphanumeric file names
def alphanumeric_sort(file_name):
    parts = file_name.split(".")[0].split("_")
    if len(parts) == 2 and parts[0] == "frame":
        return int(parts[1])
    else:
        return file_name

# Sort the JPG files based on the alphanumeric sequence in the file names
jpg_files.sort(key=alphanumeric_sort)

# Create a list to store the frames
frames = []

# Iterate through the JPG files
for jpg_file in jpg_files:
    # Read the JPG image using OpenCV
    img = cv2.imread(os.path.join(input_folder, jpg_file))
    # Convert the image to RGB using PIL (OpenCV reads images in BGR format)
    rgb_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # Resize the image to the desired resolution (1280x720)
    resized_img = rgb_img.resize((1280, 720))
    # Convert the image back to BGR format
    resized_img_bgr = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)
    # Append the resized frame to the list of frames
    frames.append(resized_img_bgr)

# Calculate the new frame rate based on the desired duration
num_frames = len(frames)
fps = num_frames / duration

# Calculate the new duration based on the frame rate and number of frames
new_duration = num_frames / fps

# Create a VideoWriter object to write the frames into an MP4 file
height, width, _ = frames[0].shape
video_writer = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

# Write the frames to the video file
for frame in frames:
    video_writer.write(frame)

# Release the VideoWriter
video_writer.release()

print(f"MP4 video created successfully! Duration: {new_duration:.2f} seconds.")
