import pandas as pd 

def cels_from_fahr(fahr):
    #Convert a Fahrenheit temperature to
    #Celsius and return the Celsius temperature.
    
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)

def go_to_beach(row):
    if row['day'] == 'sunday':
        return 'no'
    elif row['temp'] > 70:
        return 'yes'
    else:
        return 'no'

temps = pd.read_csv('temps.csv')

temps['beach_trip'] =temps.apply(go_to_beach, axis=1)
# print(temps)

# temps['celsius'] = temps['temps'].apply(cels_from_fahr)

print(temps)
