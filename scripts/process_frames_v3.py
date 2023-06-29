import os
from PIL import Image
from PIL import ImageFilter

# Specify the input folder containing the frames
input_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames"

# Specify the output folder for the processed frames
output_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames\processed"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        # Open the input image
        input_image_path = os.path.join(input_folder, filename)
        input_image = Image.open(input_image_path)

        # Apply edge detection using the Canny filter
        edges = input_image.filter(ImageFilter.FIND_EDGES)

        # Save the processed image to the output folder
        output_image_path = os.path.join(output_folder, filename)
        edges.save(output_image_path)

        print(f"Processed: {filename}")

print("Processing completed.")
