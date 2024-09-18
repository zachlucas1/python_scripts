#working with rounding numbers
user_input_number = input('Enter number to round: ')
value_number_to_round = float(user_input_number)

#.5 does to the tenth 
#.05 does to the hundreth 
#.005 does to the thousandth
round_precision = .005

#if you want to do to the hundreth or thousandth, you have to change
#it to float below
rounded_number = int(value_number_to_round + round_precision)
output_string = "Here is the number round to the nearest: " + str(rounded_number)
print(output_string)
print(f'Here is the number round to the nearest: {rounded_number:.3f}')
print('Here is the number round to the nearest: {}'.format( rounded_number))



cars = 3
people = 8

people_per_car = people / cars

print(f'There are {people_per_car} people in each car.')
# it will print a super long number

# round to one decimal
print(f'There are {people_per_car:.1f} people in each car.')
# output: There are 2.7 people in each car.

# round to two decimals
print(f'There are {people_per_car:.2f} people in each car.')
# output: There are 2.67 people in each car.

# round to three decimals
print(f'There are {people_per_car:.3f} people in each car.')
# output: There are 2.667 people in each car.



distance = 9 * 1205 * 18

# Scientific notatoin with 3 digits of precision
print(f'The distance is: {distance:.3e} meters.')
# Output: the distance is: 1.952e+05 meters.

# Scientific notatoin with 3 digits of precision
print(f'The distance is: {distance:.6e} meters.')
# Output: the distance is: 1.952100e+05 meters.



big_number = 123456789

# Display without formatting
print(f'The number it {big_number}')
# Output: The number is 123456789

# Display with "," formatting
print(f'The number it {big_number:,}')
# Output: The number is 123,456,789

# Display with "_" formatting
print(f'The number it {big_number:_}')
# Output: The number is 123_456_789



import math

radius = 5
area = math.pi * (radius ** 2)
print(f'The area is: {area}')
# Output: The area is: 78.53981633974483



import math

weight = 1.65

lower = math.floor(weight)
print(lower)
# Output: 1

higher = math.ceil(weight)
print(higher)
# Output: 2

