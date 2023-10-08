import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_IN_EACH_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_IN_EACH_LINE):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in quick_pick:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(random_number)
    print(" ".join([f"{str(number):>2}" for number in sorted(quick_pick)]))
