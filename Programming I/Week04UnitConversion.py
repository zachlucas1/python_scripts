#Title: Unit Conversion
#Author: Zach Lucas
#Description: User inputs degrees fahrenheit
#and it outputs in degrees celsius

#User inputs degrees fahrenheit
degrees_f = float(input("What is the tempurature in Fahrenheit? "))

#That nice calculation
degrees_c = (degrees_f - 32) * 5 / 9

#Outputs degrees calsius
print(f'The tempurature in celsius is {degrees_c:.1f} degrees.')
print(' ')
