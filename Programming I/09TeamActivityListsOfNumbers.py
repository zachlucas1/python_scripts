numbers = []
number = -1

while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers.append(number)

smallest_number = 999999999999999999999999
for number in numbers:
    if number > 0 and number < smallest_number:
        smallest_number = number

print(f'The sum is: {sum(numbers)}')
print(f'The average is: {(sum(numbers))/(len(numbers))}')
print(f'The largest number is: {max(numbers)}')
print(f'The smallest positive number is: {smallest_number}')

sorted_list = sorted(numbers)
print(f'The sorted list is:')
for number in sorted_list:
    print(number)
