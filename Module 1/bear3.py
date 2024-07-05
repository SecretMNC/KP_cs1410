from PIL import Image

# Using bears_copy.jpg as the original image
filename = 'bears_copy.jpg'
filepath = f"./{filename}"

# Using Red_balloon.png as the image to transpose on bears_copy.jpg
bln_name = 'Red_balloon.png'
bln_path = f"./{bln_name}"

# Outputting new image as bears3.jpg
file_out = 'bears3.jpg'
file_out_path = f"./{file_out}"

# Load the bear image, and get its size and color mode.
orig_image = Image.open(filepath)
width, height = orig_image.size
mode = orig_image.mode

# Load all pixels from the image.
orig_pixel_map = orig_image.load()

# Load the balloon image, and get its size..
bln_image = Image.open(bln_path)
bln_w, bln_h = bln_image.size

# Create a new image matching the original image's color mode, and size.
#   Load all the pixels from this new image as well.
new_image = Image.new('RGBA', (width, height))
new_pixel_map = new_image.load()

# Create an offset for the x and y coordinate to place the balloon.
offset = ((width - bln_w) // 2, (height - bln_h) // 3)

# Copy base image to new image
for x in range(width):
    for y in range(height):
        # Copy the original pixel to the new pixel map.
        new_pixel_map[x, y] = orig_pixel_map[x, y]

# Modify only the pixels that the red balloon will occupy.
new_image.paste(bln_image, offset)

# Make sure the color mode is compatiable with .JPG
final_image = new_image.convert("RGB")
final_image.save(file_out_path)