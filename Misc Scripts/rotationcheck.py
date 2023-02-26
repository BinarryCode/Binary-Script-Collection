# Writes a TEXTURES.txt lump with sprites that are rotated or flipped from another.
# (made with ChatGPT)

import os
from PIL import Image, ImageOps
import struct
sprites_used_array = []
sprites_duplicate_array = []

# Function to check if image is flipped horizontally
def is_flipped_horizontally(image, other_image):
    flipped_image = ImageOps.mirror(image)
    return hash(flipped_image.tobytes()) == hash(other_image.tobytes())

# Function to check if image is flipped vertically
def is_flipped_vertically(image, other_image):
    flipped_image = ImageOps.flip(image)
    return hash(flipped_image.tobytes()) == hash(other_image.tobytes())

# Function to check if image is rotated by a multiple of 90 degrees
def is_rotated(image, other_image):
    for angle in [0, 90, 180, 270, -90, -180]:
        rotated_image = image.rotate(angle, resample=Image.BILINEAR)
        if hash(rotated_image.tobytes()) == hash(other_image.tobytes()):
            return angle
    return None


# Prompt user for sprites folder
folder_path = input("Enter the path to the sprites folder: ")

# Get all PNG files in the folder
png_files = [file for file in os.listdir(folder_path) if file.endswith(".png")]

# Sort the list of PNG files
png_files.sort()

# Iterate through every pair of PNG files in the folder
with open("TEXTURES.txt", "a") as file:
    for i in range(len(png_files)):
        current_file = os.path.join(folder_path, png_files[i])
        current_image = Image.open(current_file)
        for j in range(i+1, len(png_files)):
            next_file = os.path.join(folder_path, png_files[j])
            with open(str(next_file), "rb") as nextImg:
                # get X offset
                nextImg.seek(0x2C)
                x_offset = nextImg.read(1)
                x_offset = struct.unpack('b', x_offset)[0]
                
                # get Y offset
                nextImg.seek(0x30)
                y_offset = nextImg.read(1)
                y_offset = struct.unpack('b', y_offset)[0]
            nextImg.close()
            next_image = Image.open(next_file)
        
            # Check if the current image is flipped horizontally or vertically compared to the next image
            flipped_horizontally = is_flipped_horizontally(current_image, next_image)
            flipped_vertically = is_flipped_vertically(current_image, next_image)
        
            # Check if the current image is rotated by a multiple of 90 degrees compared to the next image
            rotated = is_rotated(current_image, next_image)
            
            # Get x and y offset of next_image.
            xOff = x_offset
            yOff = y_offset
            
            # Write info to txt file if any flip or rotation was found
            if (flipped_horizontally or flipped_vertically) or rotated is not None:
                if png_files[j] not in sprites_duplicate_array:
                    print(f"Sprite \"{png_files[j]}\" is flipped ")
                    sprite_b_width, sprite_b_height = next_image.size

                    if flipped_horizontally and flipped_vertically:
                        print("horizontally and vertically.\n")
                    elif flipped_horizontally:
                        print("horizontally.\n")
                    else:
                        print("vertically.\n")

                    # Write TEXTURES format for flipped sprite
                    if png_files[i] not in sprites_used_array:
                        sprites_used_array.append(png_files[i])
                    
                    if png_files[j] not in sprites_duplicate_array:
                        sprites_duplicate_array.append(png_files[j])
                    
                    file.write(f'Sprite "{png_files[j]}", {sprite_b_width}, {sprite_b_height}\n')
                    file.write('{\n')
                    file.write(f'	Offset {xOff}, {yOff}\n')
                    file.write(f'	Patch "{png_files[i]}", 0, 0\n')
                    file.write('	{\n')
                    if flipped_horizontally:
                        file.write('		FlipX\n')
                    if flipped_vertically:
                        file.write('		FlipY\n')
                    if rotated is not None:
                        file.write(f'		Rotate {rotated}\n')
                    file.write('	}\n')
                    file.write('}\n\n')
    print("Info written to TEXTURES.txt")
    print("Unique sprites: " + str(sprites_used_array))