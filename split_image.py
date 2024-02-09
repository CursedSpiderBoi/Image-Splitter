import os
import sys
from PIL import Image

def split_image(image_path, rows, columns):
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    # Calculate the width and height of each part
    part_width = img_width // columns
    part_height = img_height // rows
    
    # Extract filename without extension
    filename = os.path.splitext(os.path.basename(image_path))[0]
    
    # Iterate through each part
    for row in range(rows):
        for col in range(columns):
            # Calculate the cropping region
            left = col * part_width
            upper = row * part_height
            right = left + part_width
            lower = upper + part_height
            
            # Crop the image
            part = img.crop((left, upper, right, lower))
            
            # Save the cropped part with filename prefix
            part.save(f"{filename}-{row}-{col}.png")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python split_image.py <image_path> <rows> <columns>")
        sys.exit(1)

    image_path = sys.argv[1]
    rows = int(sys.argv[2])
    columns = int(sys.argv[3])

    split_image(image_path, rows, columns)
