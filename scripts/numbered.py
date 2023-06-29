import os
from PIL import Image

# Function to convert an image to ASCII art
def convert_image_to_ascii(input_image):
    # Resize the image for better ASCII representation
    width, height = input_image.size
    aspect_ratio = height / width
    new_width = 200  # Adjust the desired width
    new_height = int(new_width * aspect_ratio)
    resized_image = input_image.resize((new_width, new_height))

    # Define the ASCII numbers to represent different shades of gray
    ascii_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Convert the image to ASCII art
    ascii_art = ''
    for y in range(new_height):
        for x in range(new_width):
            pixel = resized_image.getpixel((x, y))
            gray_value = (pixel[0] + pixel[1] + pixel[2]) // 3
            ascii_number = ascii_numbers[gray_value * len(ascii_numbers) // 256]
            ascii_art += str(ascii_number)
        ascii_art += '\n'

    return ascii_art


# Specify the folder path containing the input images
folder_path = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames"

# Specify the output folder for the ASCII art
output_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\numbered"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg"):
        # Open the input image
        input_image_path = os.path.join(folder_path, file_name)
        input_image = Image.open(input_image_path)

        # Convert the image to ASCII art
        ascii_art = convert_image_to_ascii(input_image)

        # Save the ASCII art to a text file
        output_file_name = file_name.replace(".jpg", ".txt")
        output_file_path = os.path.join(output_folder, output_file_name)
        with open(output_file_path, 'w') as file:
            file.write(ascii_art)

        print(f"ASCII art created for {file_name}")

print("Conversion completed.")
