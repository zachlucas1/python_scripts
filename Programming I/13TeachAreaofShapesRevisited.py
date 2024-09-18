#Title: Areas of Shapes Revisited
#Author: Zach Lucas
#Description: User inputs various inputs of length and width
#to output area as a function

import math

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * (radius * radius)

def area_triangle(base, height):
    return (base * height) / 2

shape = ''

while shape !='quit':
    shape = input('What shape do you have? ').lower()

    if shape == 'square':
        side = float(input('What is the length of the side? '))
        print(f'The area is {area_square(side)}')

    elif shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        print(f'The area is: {area_rectangle(length, width)}')

    elif shape == 'circle':
        radius = float(input('What is the radius? '))
        print(f'The area is {area_circle(radius):.1f}')

    # For some reason this doesnt work
    # elif shape == 'triangle':
    #     base = float(input('What is the base? '))
    #     height = float(input('What is the height? '))
    #     print(f'The area is {area_triangle(base, height)}')