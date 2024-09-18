#Name: Zach Lucas
#Assignment: 02 Prove: Validate User Input
#Description: User inputs the width, aspect ratio, and diameter of a tire
# and it outputs an answer

#imports math so that we can use math.pi
import math

#asks tire brand that outputs in the print statement later
tire_brand = input('What brand of tire is this? ').capitalize()

#Get width from user
minimum = 180
maximum = 400

valid = False
while not valid:
    text = input('Enter the width of the tire in mm (ex 205): ')

    if text.isdecimal():
        width = int(text)

        if width < minimum:
            print(f'"{width}" is too small. Please enter a positive integer between {minimum} and {maximum}.')
        elif width > maximum:
            print(f'"{width}" is too large. Please enter a positive integer between {minimum} and {maximum}.')
        else:
            valid = True
    else:
        print(f'"{text}" is not a positive integer. Please enter an integer beween {minimum} and {maximum}.')

#Get aspect ratio from user
minimum = 45
maximum = 70

valid = False
while not valid:
    text = input('Enter the aspect ratio of the tire (ex 60): ')

    if text.isdecimal():
        aspect_ratio = int(text)

        if aspect_ratio < minimum:
            print(f'"{aspect_ratio}" is too small. Please enter a positive integer between {minimum} and {maximum}.')
        elif aspect_ratio > maximum:
            print(f'"{aspect_ratio}" is too large. Please enter a positive integer between {minimum} and {maximum}.')
        else:
            valid = True
    else:
        print(f'"{text}" is not a positive integer. Please enter an integer beween {minimum} and {maximum}.')

#Get diameter from user
minimum = 12
maximum = 28

valid = False
while not valid:
    text = input('Enter the diameter of the tire in inches (ex 15): ')

    if text.isdecimal():
        diameter = int(text)

        if diameter < minimum:
            print(f'"{diameter}" is too small. Please enter a positive integer between {minimum} and {maximum}.')
        elif diameter > maximum:
            print(f'"{diameter}" is too large. Please enter a positive integer between {minimum} and {maximum}.')
        else:
            valid = True
    else:
        print(f'"{text}" is not a positive integer. Please enter an integer beween {minimum} and {maximum}.')

#Math for the equation split into two parts and then combined later for final answer.
part1 = math.pi * (width**2) * aspect_ratio
part2 = (width * aspect_ratio) + (2540 * diameter)

answer = (part1 * part2) / 10000000

#Outputs answer with one decimal place.
print()
print(f'The aproximate volume of your {tire_brand} tire is {answer:.1f} millimeters.')
print()