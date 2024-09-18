#OG VANILLA PROGRAM WITH NO GUI
import datetime

current_time = datetime.datetime.now()
current_hour = int(current_time.strftime('%H'))

def main():
    # print(current_hour)
    ratio = get_carbs()
    correction = get_glucose()
    calculate_insulin(ratio, correction)


def get_carbs():
    ratio = 0
    carbs = int(input('Please enter carbs: '))
    if current_hour <= 11:
        ratio = carbs / 6
    elif (current_hour > 11) and (current_hour <= 16):
        ratio = carbs / 8
    elif current_hour > 16:
        ratio = carbs / 7
    return round(ratio, 1)


def get_glucose():
    glucose = int(input('Please enter current glucose reading: '))
    correction = 0
    if current_hour <= 14:
        correction = (glucose - 130) / 32
    elif current_hour >= 14:
        correction = (glucose - 130) / 30
    return round(correction, 1)


def calculate_insulin(ratio, correction):
    insulin = ratio + correction
    print(f'Please take {insulin} units of insulin.')
    return insulin


main()