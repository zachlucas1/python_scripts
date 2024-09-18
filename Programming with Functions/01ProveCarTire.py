#Name: Zach Lucas
#Assignment: 01 Prove Milestone: Review Python
#Description: User inputs the width, aspect ratio, and diameter of a tire
# and it outputs an answer

import math

#Asks user for measurements, if they enter something lower than zero it doesn't
#work and it gives them a chance to try again.
width = int(input('Enter the width of the tire in mm (ex 205): '))
if width < 0:
    print('That is not a valid input, please try again')
    print('')
    width = int(input('Enter the width of the tire in mm (ex 205): '))

aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
if aspect_ratio < 0:
    print('That is not a valid input, please try again')
    aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))

diameter = int(input('Enter the diameter of the tire in inches (ex 15): '))
if diameter < 0:
    print('That is not a valid input, please try again')
    diameter = int(input('Enter the diameter of the tire in inches (ex 15): '))

#Math for the equation split into two parts and then combined later for final answer.
part1 = math.pi * (width**2) * aspect_ratio
part2 = (width * aspect_ratio) + (2540 * diameter)

answer = (part1 * part2) / 10000000

#Outputs answer with one decimal place.
print(' ')
print(f'{answer:.1f}')