"""
guitar_test.py

Estimated Time: 45 mins
Start Time: 9:02pm
Finish Time:
Actual Time:
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2022

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 6500.50)
print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age(CURRENT_YEAR)}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(CURRENT_YEAR)}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(CURRENT_YEAR)}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(CURRENT_YEAR)}")
