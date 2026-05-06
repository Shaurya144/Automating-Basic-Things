
# The main tool used is pytesseract (wrapper for Tesseract OCR engine)

# Installing required tools

# Install pytesseract (Python library)
# pip install pytesseract

# Install Pillow (image processing)
# pip install pillow

# Install Tesseract OCR separately (not a Python package)


# Importing modules

import pytesseract
from PIL import Image


# Basic OCR usage

# Open an image file
img = Image.open('image.png')

# Extract text from the image
text = pytesseract.image_to_string(img)

print(text)


# How OCR works (concept)

# OCR scans images and tries to recognize letters and words
# Accuracy depends on image quality, font, and clarity


# Improving OCR accuracy

# Use clear, high-resolution images
# Avoid blurry or distorted text
# Use simple fonts if possible

# Convert image to grayscale
img = img.convert('L')

# Apply thresholding (optional preprocessing)
# Makes text stand out more clearly


# Working with different image formats

# Supported formats include PNG, JPG, BMP, etc.
img = Image.open('photo.jpg')


# Getting detailed OCR data

# Returns info about each detected word
data = pytesseract.image_to_data(img)

# Returns bounding box info
boxes = pytesseract.image_to_boxes(img)


# Searching for specific text in images

text = pytesseract.image_to_string(img)

if "Hello" in text:
    print("Found the word!")


# Using OCR in automation

# Extract text from screenshots
screenshot = Image.open('screenshot.png')
text = pytesseract.image_to_string(screenshot)

# Useful for:
# reading text from scanned documents
# automating tasks involving screenshots
# extracting data from images


# Limitations of OCR

# Not always 100% accurate
# Struggles with:
# low resolution images
# handwriting
# complex backgrounds


# Key Takeaways

# pytesseract enables OCR in Python
# Pillow is used to open and process images
# OCR converts images into readable text
# preprocessing images improves accuracy
# useful for automation tasks involving text in images
