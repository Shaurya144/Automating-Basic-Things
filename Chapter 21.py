import matplotlib.pyplot as plt


# Basic Line Graph

x_values = [1, 2, 3, 4]

y_values = [10, 20, 25, 30]

# plt.plot(x_values, y_values)

# plt.show()


# Labels and Title

# plt.title("Sales")

# plt.xlabel("Month")

# plt.ylabel("Profit")


# Bar Chart

languages = ["Python", "Java", "C++"]

users = [100, 70, 50]

# plt.bar(languages, users)

# plt.show()


# Pie Chart

sizes = [50, 30, 20]

labels = ["Python", "Java", "C++"]

# plt.pie(sizes, labels=labels)

# plt.show()


# Saving Graphs

# plt.savefig("graph.png")


# Pillow

"""
Pillow edits images.

Module:
PIL
"""

# pip install pillow

from PIL import Image


# Opening Images

# image_obj = Image.open("cat.png")

# print(image_obj.size)

# print(image_obj.filename)


# Image Size

"""
size returns:
(width, height)
"""


# Cropping Images

# cropped = image_obj.crop(
#     (0, 0, 100, 100)
# )

# cropped.show()


# Copying Images

# copied = image_obj.copy()


# Resizing Images

# resized = image_obj.resize(
#     (300, 300)
# )

# resized.show()


# Rotating Images

# rotated = image_obj.rotate(90)

# rotated.show()


# Flipping Images

# flipped = image_obj.transpose(
#     Image.FLIP_LEFT_RIGHT
# )

# flipped.show()


# Saving Images

# image_obj.save("new_image.png")


# Drawing on Images

from PIL import ImageDraw

# draw = ImageDraw.Draw(image_obj)

# draw.line((0, 0, 100, 100))

# draw.rectangle((20, 20, 80, 80))

# draw.text((10, 10), "Hello")


# Fonts

from PIL import ImageFont

# font = ImageFont.truetype(
#     "arial.ttf",
#     20
# )

# draw.text(
#     (50, 50),
#     "Python",
#     fill="white",
#     font=font
# )


# Colors

"""
Common colors:
red
blue
white
black
green
"""


# RGBA Colors

"""
RGBA format:

(red, green, blue, alpha)

Example:
(255, 0, 0, 255)
"""


# Common Image Formats

"""
PNG
JPEG
GIF
BMP
"""


# Mini Image Example

from PIL import Image

# image = Image.open("photo.png")

# resized = image.resize((200, 200))

# resized.save("small_photo.png")


print("Chapter 21 notes loaded.")
