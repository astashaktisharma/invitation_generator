#import here
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import os

# The image that we’ll be using as the base/template for the invitations
base_image_path = "5th_april.png"

# This is the text file where we list all the names (one per line)
name_list_path = "names.txt"

# The font file we'll use for the names (can download fonts from Google Fonts)
font_path = "PlaywriteDEGrund-VariableFont_wght.ttf"

# Max and min font sizes — name length will determine which one we use
max_font_size = 250
min_font_size = 100

# set the max width
max_text_width = 700

# Color for the final sharp text on top (currently black)
text_color = (0, 0, 0)

# Folder where all generated invites (PNG/PDF) will be saved
output_folder = "invitations"
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Read all names from the text file, strip out extra whitespace or blank lines
with open(name_list_path, "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

# Function to figure out how big the name font should be
def adjust_font(draw, text):
    # If the name is short (<= 20 characters), go with the max font size (if it fits)
    if len(text) <= 20:
        font = ImageFont.truetype(font_path, max_font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_text_width:
            return font  # Looks good, use it!

    # If it doesn't fit or name is longer, gradually decrease size until it fits
    size = max_font_size
    while size >= min_font_size:
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_text_width:
            return font  # Found a good size!
        size -= 2  # Shrink the font a bit and try again

    # If nothing else works, return the minimum size font
    return ImageFont.truetype(font_path, min_font_size)

# Ask the user what kind of output they want
print("\nWhat would you like to generate?")
print("1 - PNG only")
print("2 - PDF only")
print("3 - Both PNG and PDF")
choice = input("Enter your choice (1/2/3): ").strip()

# These are the center coordinates where the name should be placed
center_x = 860
center_y = 600

# Loop through every name and generate a personalized card
for name in names:
    # Start fresh for each name — open a clean copy of the base image
    img = Image.open(base_image_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Pick the font size that fits the name nicely
    font = adjust_font(draw, name)

    # Measure the size of the text to position it perfectly in the center
    bbox = draw.textbbox((0, 0), name, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    position = (center_x - w // 2, center_y - h // 2)

    # simulate thickness by drawing the name lots of times around itself
    stroke_color = (230, 130, 255)  # This is the shadow/bold stroke color
    for dx in range(-9, 10):        # This gives us a 19x19 grid = 361 layers
        for dy in range(-9, 10):
            draw.text((position[0] + dx, position[1] + dy), name, fill=stroke_color, font=font)

    # Draw the actual name on top in the main color, perfectly centered
    draw.text(position, name, fill=text_color, font=font)

    # Export the final PNG if the user chose that option
    if choice in ["1", "3"]:
        img.save(os.path.join(output_folder, f"{name}_invite.png"))

    # Export the PDF version if requested
    if choice in ["2", "3"]:
        # Temporarily save as PNG so we can embed it into the PDF
        pdf = FPDF(unit="pt", format=[img.width, img.height])
        pdf.add_page()
        temp_img_path = os.path.join(output_folder, f"{name}_temp.png")
        img.save(temp_img_path)
        pdf.image(temp_img_path, 0, 0)
        pdf.output(os.path.join(output_folder, f"{name}_invite.pdf"))
        os.remove(temp_img_path)  # Clean up temp image after making PDF

print("All invitations created!")
