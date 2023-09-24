import random
MINIMUM_SCORE = 1
MAXIMUM_SCORE = 100


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    result = determine_result(score)
    print(f"Random score: {random_score}, Result: {result}")


def determine_result(score):
    if 100 >= score >= 90:
        result = "Excellent!"
    elif score >= 50:
        result = "Passable."
    elif score >= 0:
        result = "Bad!!!"
    else:
        result = "Invalid score."

    return result


main()
