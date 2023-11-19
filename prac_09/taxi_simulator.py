"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """
    Allow the user to choose a taxi and drive around, and show the total bill in the end.
    """
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    taxis[current_taxi].start_fare()
                    taxis[current_taxi].drive(distance)
                    current_bill = taxis[current_taxi].get_fare()
                    print(f"Your {taxis[current_taxi].name} trip costs you ${current_bill:.2f}")
                    total_bill += current_bill
                except ValueError:
                    print("Invalid input")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """
    Display the list of all taxis.
    """
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, current_taxi):
    """
    Let the user choose a taxi from the list. If the choice is invalid,
    return the current taxi.
    """
    try:
        choice = int(input("Choose taxi: "))
        if choice >= len(taxis):
            print("Invalid taxi choice")
            choice = current_taxi
    except ValueError:
        print("Invalid input")
        choice = current_taxi
    return choice


if __name__ == '__main__':
    main()
