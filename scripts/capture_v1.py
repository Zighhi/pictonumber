import os
from PIL import Image, ImageDraw, ImageFont

# Specify the folder path containing the text files
folder_path = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\numbered"

# Specify the output folder for the screenshots
output_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\screenshots"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the desired capture dimensions
capture_width = 1410  # Adjust the desired width
capture_height = 1710  # Adjust the desired height

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        # Open the text file
        text_file_path = os.path.join(folder_path, file_name)
        with open(text_file_path, 'r') as file:
            text_content = file.read()

        # Calculate the required image dimensions based on the text content
        font_size = 12  # Adjust the desired font size
        font = ImageFont.truetype('arial.ttf', font_size)
        text_width, text_height = font.getsize_multiline(text_content)

        # Calculate the starting position for the text
        start_x = (capture_width - text_width) // 2
        start_y = (capture_height - text_height) // 2

        # Create an image with the desired resolution
        image = Image.new('RGB', (capture_width, capture_height), color=(255, 255, 255))
        image_draw = ImageDraw.Draw(image)

        # Draw the text on the image
        image_draw.multiline_text((start_x, start_y), text_content, font=font, fill=(0, 0, 0))

        # Resize the image for capture dimensions
        resized_image = image.resize((1280, 720), Image.LANCZOS)

        # Save the screenshot as an image file
        output_file_name = file_name.replace(".txt", ".jpg")
        output_file_path = os.path.join(output_folder, output_file_name)
        resized_image.save(output_file_path)

        print(f"Screenshot created for {file_name}")

print("Screenshot generation completed.")
