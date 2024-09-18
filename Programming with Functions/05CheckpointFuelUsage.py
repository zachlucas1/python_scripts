#mpg equation
def miles_per_gallon(start, end, gallons):
    mpg = abs(end - start) / gallons
    return mpg

#equation for converting miles per gallon to liters per 100 kilometers
def lp100k_from_mpg(mpg):
    lpk100k = 235.215 / mpg
    return lpk100k

def main():
    # Get an odometer value in U.S. miles from the user.
    start = float(input('Enter the first odometer reading (in miles): '))

    # Get another odometer value in U.S. miles from the user.
    end = float(input('Enter the second odometer reading (in miles): '))

    # Get a fuel amount in U.S. gallons from the user.
    gallons = float(input('Enter the amount of fuel used (in gallons): '))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start, end, gallons)

    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 1)
    
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(f'{mpg} miles per gallon')
    print(f'{lp100k} liters per 100 kilometers')


# Call the main function so that
# this program will start executing.
main()