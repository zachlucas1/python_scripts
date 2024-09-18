# Import necessary modules.
import csv
import math
from datetime import date, datetime


def compute_age(birth):
    """Compute and return a person's age in years.

    param birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    """
    birthdate = datetime.strptime(birth, "%Y-%m-%d").date()
    now = date.today()
    diff = now - birthdate
    years = math.floor(diff.days / 365.25)
    return years


def kg_from_lb(lb):
    """Convert a mass in US pounds to kilograms.
    param lb: a mass in US pounds
    """
    weight_kg = lb * 0.45359237
    return weight_kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    param inch: a length in inches
    """
    cm = inch * 2.54
    return cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass
    index (bmi). weight and height must be in
    kilograms and centimeters, respectively.
    """
    bmi = (10000 * weight) / height ** 2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic
    rate (bmr). weight must be in kilograms, height
    must be in centimeters, and age must be in years.
    """
    bmr = 0
    if gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

    if gender == 'F':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr


def main():
    # Print this header:
    # Gender,Age (years),Weight (kg),Height (cm),BMI,BMR
    print('Gender, Age (years), Weight (kg), Height (cm), BMI, BMR')
    # Open the fitness.csv file for reading.
    with open('fitness.csv') as infile:
        fitness_file = csv.reader(infile)

        # Use the csv module to get a reader object.
        #skips first line
        next(fitness_file)

        for line in fitness_file:
            gender = line[0]
            birth_date = line[1]
            weight_lbs = float(line[2])
            height_in = float(line[3])

            age = compute_age(birth_date) - 1
            weight_kg = kg_from_lb(weight_lbs)
            height_cm = cm_from_in(height_in)
            bmi = body_mass_index(weight_kg, height_cm)
            bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

            print(f'{gender}, {age}, {weight_kg:.2f}, {height_cm:.1f}, {bmi:.1f}, {bmr:.1f}')
        # Process each row in the csv file by doing the following:
            # 1. Call the compute_age, kg_from_lb, cm_from_in,
            #    body_mass_index, and basal_metabolic_rate
            #    functions as necessary.

            # 2. Print the gender, age in years, weight in
            #    kilograms, height in centimeters, body mass
            #    index, and basal metabolic rate.

# Call the main function so that
# this program will start executing.
main()