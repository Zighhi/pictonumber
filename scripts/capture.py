import os
from PIL import Image, ImageDraw, ImageFont

# Specify the folder path containing the text files
folder_path = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\numbered"

# Specify the output folder for the screenshots
output_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\screenshots"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the desired capture dimensions
capture_width = 1210  # Adjust the desired width
capture_height = 1200  # Adjust the desired height

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        # Open the text file
        text_file_path = os.path.join(folder_path, file_name)
        with open(text_file_path, 'r') as file:
            text_content = file.read()

        # Create an image with the desired resolution
        image = Image.new('RGB', (capture_width, capture_height), color=(255, 255, 255))
        image_draw = ImageDraw.Draw(image)

        # Load the default monospaced font
        font = ImageFont.load_default()

        # Calculate the number of rows and columns for the text content
        rows = text_content.count('\n') + 1
        columns = len(text_content) // rows

        # Calculate the starting position for the text
        text_width, text_height = image_draw.textsize(text_content[0], font=font)
        start_x = (capture_width - columns * text_width) // 2
        start_y = (capture_height - rows * text_height) // 2

        # Draw the text on the image
        for i, char in enumerate(text_content):
            x = start_x + (i % columns) * text_width
            y = start_y + (i // columns) * text_height
            image_draw.text((x, y), char, font=font, fill=(0, 0, 0))

        # Resize the image for capture dimensions
        resized_image = image.resize((1280, 720), Image.LANCZOS)

        # Save the screenshot as an image file
        output_file_name = file_name.replace(".txt", ".jpg")
        output_file_path = os.path.join(output_folder, output_file_name)
        resized_image.save(output_file_path)

        print(f"Screenshot created for {file_name}")

print("Screenshot generation completed.")
