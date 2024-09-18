def main():
    #Create and print a list named fruit.
    fruit = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit}")

    #This reverses the fruit order
    fruit.reverse()
    print(f'Reversed: {fruit}')

    #This adds orange to the fruit list
    fruit.append('orange')
    print(f'Append Orange: {fruit}')

    #This inserts cherry before apple on the list
    position = fruit.index('apple')
    fruit.insert(position, 'cherry')
    print(f'Insert cherry: {fruit}')

    #This removes banana from the list
    fruit.remove('banana')
    print(f'Remove Banana: {fruit}')

    #This removes that last element in the list and then prints it
    popped = fruit.pop()
    print(f'{popped} {fruit}')

    #This sorts the list in alphabetical order
    fruit.sort()
    print(f'Sorted: {fruit}')

    #This clears the whole list
    fruit.clear()
    print(f'Cleared: {fruit}')

main()