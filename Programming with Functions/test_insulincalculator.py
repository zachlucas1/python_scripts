from testinsulin import get_carbs, get_glucose, calculate_insulin
import pytest
import datetime

current_time = datetime.datetime.now()
current_hour = int(current_time.strftime('%H'))

def test_carbs(carbs):
    if current_hour <= 11:
        assert get_carbs(25) == 4.2
    elif (current_hour > 11) and (current_hour < 16):
        assert get_carbs(25) == 3.1
    elif current_hour > 16:
        assert get_carbs(25) == 3.6


def test_glucose(glucose):
    if current_hour <= 14:
        assert get_glucose(150) == 0.6
    elif current_hour >= 14:
        assert get_glucose(150) == 0.7


pytest.main(["-v", "--tb=no", "test_insulincalculator.py"])