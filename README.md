# Invitation Card Generator

This Python script allows you to automatically generate personalized invitation cards from a base image and a list of names. The names are styled and centered on the template using a custom font, with optional bold effects applied. You can choose to export each card as a PNG, PDF, or both.

## Features

- Uses a custom image as the background template  
- Accepts a `.ttf` font file of your choice  
- Automatically resizes font based on name length
- Applies a bold text effect by layering multiple strokes  
- Outputs high-quality PNG and PDF versions  
- Simple text-based input via a `names.txt` file  

## How It Works

1. You provide an image file (e.g., `5th_april.png`) to use as your base template.  
2. You list all names in a plain text file called `names.txt`, with one name per line.  
3. You run the Python script (`invitation_maker.py`).  
4. When prompted, you choose whether you want PNG files, PDFs, or both.  
5. The script places each name in a visually centered position on the image, adjusting font size as needed.  
6. Output files are saved in an auto-created `invitations/` folder.

## Installation

1. Make sure you have Python 3 installed.  
2. Install the required libraries: pip install pillow fpdf 
3. Clone this repository or download the files manually.

## Project Structure
invitation-generator/
├── invitation_maker.py
├── names.txt
├── 5th_april.png
├── PlaywriteDEGrund-VariableFont_wght.ttf
└── invitations/ (auto-created)

## Usage

1. Add your invitation background image to the project folder. 
2. Create or edit `names.txt` with one name per line.  
3. Place your desired font file (`.ttf`) in the same folder.  
4. Run the script: python invitation_maker.py
5. Choose the output format when prompted (PNG, PDF, or both).  
6. Your customized invitation cards will appear in the `invitations/` folder.

## Customization

- To change the font or font size range, modify the `font_path`, `max_font_size`, and `min_font_size` values at the top of the script.  
- To change the position of the name overlay, adjust the `center_x` and `center_y` values.  
- The bold effect is created by layering multiple copies of the name slightly offset from each other. You can control the intensity of this effect by adjusting the range in the nested `for dx`, `dy` loop.


