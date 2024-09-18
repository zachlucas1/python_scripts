import pandas as pd

def main():
    # pandas reads the file and puts it into the data_frame variable
    data_frame = pd.read_csv('water.csv')

### PART 1 ###

    #print the number of unique account types
    unique_account = data_frame['accountType'].unique()
    print('Unique account types:')
    print(len(unique_account), unique_account)
    print()

    #print number of unique meters
    unique_meters = data_frame['meterNumber'].unique()
    print('Unique meter numbers:')
    print(len(unique_meters), unique_meters)
    print()

### PART 2 ###

    #sum of all water used
    all_usage = data_frame['usage'].sum()
    print(f'Total water used: {all_usage}')

    #residence water sum
    residence_filter = data_frame['accountType'] == 'Residence'
    residence = data_frame[residence_filter]
    water_used = residence['usage'].sum()
    print(f'Total water used by residences: {water_used}')

    #apartment water sum
    apartment_filter = data_frame['accountType'] == 'Apartment Complex'
    apartments = data_frame[apartment_filter]
    water_used = apartments['usage'].sum()
    print(f'Total water used by apartment complexes: {water_used}')
    print()

### PART 3 ###

    #meters per account type and count how many are in each account
    meter_accounts = data_frame.drop_duplicates(subset=["meterNumber"])
    print("Meters Per Account:")
    print(meter_accounts["accountType"].value_counts())
    print()

main()