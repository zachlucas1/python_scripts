#Title: Wind Chill Calculations
#Author: Zach Lucas
#Description: User inputs tempurature and it outputs windchill in fahrenheit

#calculate wind chill
def wind_chill_equation(tempurature, speed):
    chill = 35.74 + (0.6215 * tempurature) - 35.75 * (speed ** 0.16) + 0.4275 * tempurature * (speed ** 0.16)
    return chill

#celsius conversion if needed
def celsius_conversion(tempurature):
    fahrenheit = tempurature * (9 / 5) + 32
    return fahrenheit

#gets user input
tempurature = float(input('What is the tempurature? '))
unit = input("Fahrenheit or Celsius (F/C)? ").lower()

if unit == 'c':
    tempurature = celsius_conversion(tempurature)

speed = 5

while speed <= 60:
    chill = wind_chill_equation(tempurature, speed)
    print(f'At tempurature {tempurature:.1f}F, and wind speed {speed} mph, the wind chill is {wind_chill_equation(tempurature, speed):.2f}F')
    speed += 5