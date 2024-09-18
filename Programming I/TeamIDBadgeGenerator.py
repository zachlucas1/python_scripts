#Title: ID Badge Generator
#Author: Zach Lucas
#Description: Asks user for multiple inputs of info and outputs as 
#an ID card

#Ask for information
print('Please enter the following information: ')
print(' ')
first_name = input('First Name: ')
last_name = input('Last Name: ')
email_address = input('Email address: ')
phone_number = input('Phone Number: ')
job_title = input('Job Title: ')
id_number = input('ID Number: ')
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
month = input('Month: ')
training = input('Training: ')
print(' ')

#Output the  information
print('The ID Card is:')
print('----------------------------------------')
print(f'{last_name.upper()},{first_name.capitalize()}')
print(f'{job_title.title()}')
print(f'ID:{id_number}')
print(' ')
print(f'{email_address.lower()}')
print(f'{phone_number}')
print(' ')

#The numbers space it out well
print(f'Hair: {hair_color.capitalize():15} Eyes: {eye_color.capitalize()}')
print(f'Month: {month.capitalize():14} Training: {training.capitalize()}')
print('----------------------------------------')