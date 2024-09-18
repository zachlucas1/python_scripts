# Example 1

"""def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = []
    for fahr in fahr_temps:
        cels = cels_from_fahr(fahr)
        cels_temps.append(cels)

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    #Convert a Fahrenheit temperature to
    #Celsius and return the Celsius temperature.
    
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)

main()"""



# numbers = [1, 2, 3, 4, 5]

# new_numbers = []

"""numbers = [1, 2, 3, 4, 5, 6, 7]

for n in numbers:
    print(f'{n} % 2 = {n % 2}')"""

#truthy / falsey question
"""if [2, 3]:
    print('1 is true')
else:
    print('this is false')"""

"""name = ""
while not name:
    name = input('enter your name: ')

print(f'Hello {name}')"""

"""numbers = [1, 2, 3, 4, 5, 6, 7]
for x in numbers:
    answer = x * 2
    new_numbers.append(answer)

#mapping
new_numbers = [x * 2 for x in numbers]
print(new_numbers)"""

#filtering
"""numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = [x for x in numbers if x % 2 == 1]
print(odd_numbers)"""

# Example 2

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


main()
