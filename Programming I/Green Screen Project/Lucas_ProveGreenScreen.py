#Title: Green Screen Project
#Author: Zach Lucas
#Description: This program imports 2 images, takes the "green screen" 
# out of one and combines them for an edited image.

#Imports the image libarary we need
from PIL import Image

#Load the images into a variable
image_earth = Image.open('earth.jpg')
image_spaceshuttle = Image.open('spaceshuttle.jpg')
image_new = Image.new('RGB', image_earth.size)

#Loads images into pixel variables
pixels_earth = image_earth.load()
pixels_spaceshuttle = image_spaceshuttle.load()
pixels_new = image_new.load()

#Prints width, height, and format
(width1, height1) = image_earth.size
(width2, height2) = image_spaceshuttle.size
print(f'Width of Earth: {width1}')
print(f'Height of Earth: {height1}')
print(f'Width of Spaceshuttle: {width2}')
print(f'Height of Spaceshuttle: {height2}')
print(f'Earth Format: {image_earth.format}')
print(f'Spaceshuttle Format: {image_spaceshuttle.format}')

#This goes through all the pixels
for y in range(0, 600):
    for x in range(0,800):
        (r, g, b) = pixels_spaceshuttle[x, y]
        (r1, g1, b1) = pixels_earth[x, y]
        if r < 168 and g > 178 and b < 214:
            pixels_new[x, y] = (r1, g1, b1)
        else:
            pixels_new[x, y] = (r, g, b)

#Shows the new image
image_new.show()

#Saves the new image created
image_new.save('earth_spaceshuttle.jpg')