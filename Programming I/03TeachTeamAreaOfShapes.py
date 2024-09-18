#Title: Areas of Shapes
#Author: Zach Lucas
#Description: User inputs various inputs of length and width
#to output area

#Area of a square
length1 = float(input('What is the length of side of the square? '))
area1 = length1 * length1
print(f'The area of the sqaure is: {area1}')
print(' ')

#Area of a rectangle
length2 = float(input('What is the length of the rectangle? '))
width2 = float(input('What is the width of the rectangle? '))
area2 = width2 * length2
print(f'The area of the rectangle is: {area2}')
print(' ')

#Area of the circle
import math
radius = float(input('What is the radius of the circle? '))
area3 = math.pi * (radius ** 2)
print(f'The area of the circle is: {area3}')
print(' ')

#Area of a triangle
base = float(input('What is the length of the base? '))
height = float(input('What is the length of the height? '))
area4 = (base * height) / 2
print(f'The area of the triangle is: {area4}')
print(' ')

