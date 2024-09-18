# When you physically exercise to strengthen your heart, you
# should maintain your heart rate within a range for at least 20
# minutes. To find that range, subtract your age from 220. This
# difference is your maximum heart rate per minute. Your heart
# simply will not beat faster than this maximum (220 - age).
# When exercising to strengthen your heart, you should keep your
# heart rate between 65% and 85% of your heart's maximum.

#gets users age and converts it to a float
age = float(input("Please enter your age: "))

#the maths
max_rate = (220 - age)
slowest = round(max_rate * 0.65)
fastest = round(max_rate * 0.85)

#outputs the results to user
print("When you excercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest} and {fastest} beats per minute.")