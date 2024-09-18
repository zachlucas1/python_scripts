#Title: Speed of a falling object Equation
#Author: Zach Lucas
#Description:  

# Asks user for inputs
print('Welcome to the velocity calculator. Please enter the following:')
print(' ')
m = float(input('Mass (in kg): '))
g = float(input('In m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
a = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
print(' ')

# Math v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
import math
value_c = 1/2 * (p * a * C) 
velocity = math.sqrt((m * g) / value_c) * (1 - math.exp((-math.sqrt(m * g * value_c) / m) * t))
print(' ')

# Outputs
print(f'The inner value of c is: {value_c:.3f}')
print(f'The velocity after {t:.1f} seconds is: {velocity:.3f} m/s')
print(' ')