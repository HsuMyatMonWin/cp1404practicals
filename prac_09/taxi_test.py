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
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")

    # Restart the meter (start a new fare) and then drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")

    # Test for modifications
    another_taxi = Taxi("Yarris", 200)
    another_taxi.drive(40)
    print(another_taxi)
    print(f"Current fare: ${another_taxi.get_fare()}")


if __name__ == "__main__":
    main()
