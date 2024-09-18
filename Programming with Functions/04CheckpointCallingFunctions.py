import statistics

# A list of people's height in meters.
heights = [
    1.72, 1.50, 1.96, 2.01, 1.75,
    2.11, 1.60, 1.65, 2.05, 1.50,
    1.80, 1.83, 2.05, 1.79, 1.84
]

#built in functions
number_of_heights = len(heights)
min_heights = min(heights)
max_heights = max(heights)
sum_heights = sum(heights)

mean_heights = statistics.mean(heights)
median_heights = statistics.median(heights)
mode_heights = statistics.mode(heights)

print(f'Len:{number_of_heights}')
print(f'Min: {min_heights}')
print(f'Max: {max_heights}')
print(f'Sum: {sum_heights}')
print(f'Mean: {mean_heights}')
print(f'Median: {median_heights}')
print(f'Mode: {mode_heights}')

#dumb way
# count = 0
# for height in heights:
#     count = count + 1

# print(count)