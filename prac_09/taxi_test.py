"""
Program for Testing Taxi
Date: 18/11/2023
Author: Hsu Myat Mon Win
"""
from taxi import Taxi


def main():
    """
    Test different methods of Taxi class.
    """
    # Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    print(f"{my_taxi.name} has driven {my_taxi.drive(40)}km.")

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")

    # Restart the meter (start a new fare) and then drive the car 100 km
    my_taxi.start_fare()
    print(f"{my_taxi.name} has driven {my_taxi.drive(100)}km.")

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")

    # Test for modifications
    another_taxi = Taxi("Yarris", 200)
    print(f"{another_taxi.name} has driven {another_taxi.drive(40)}km.")
    print(another_taxi)
    print(f"Current fare: ${another_taxi.get_fare()}")


main()
