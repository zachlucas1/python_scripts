import pandas as pd

def main():
    data_frame = pd.read_csv('water.csv')
    
    #prints the dtypes
    print('dtypes:')
    print(data_frame.dtypes)
    print()

    #prints the describe
    print('Describe:')
    print(data_frame.describe())
    print() 

    #prints the whole data frame
    print('Data Frame:')
    print(data_frame)
    print()

    #prints the data frame filtered by residences
    print('Account types:')
    filter = (data_frame['accountType'] == 'Residence')
    filtered_df = data_frame[filter]
    print(filtered_df)
    print()

main()