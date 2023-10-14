MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU)
    option = input(">>>").upper()

    while option != "Q":
        if option == "G":
            score = get_valid_score()
        elif option == "P":
            result = determine_result(score)
            print(f"Your result is: {result}")
        elif option == "S":
            print_stars(score)
        else:
            print("Invalid option.")
        print(MENU)
        option = input(">>>").upper()
    print("Good bye. Have a nice day :)")


def get_valid_score():
    score = int(input("Enter score: "))
    while 0 > score or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))
    return score


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


def print_stars(score):
    print("*" * score)


main()
