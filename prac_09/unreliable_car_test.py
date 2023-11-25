"""
Program for Testing Unreliable Cars
Date: 18/11/2023
Author: Hsu Myat Mon Win
"""
from unreliable_car import UnreliableCar


def main():
    """
    Test the drive method of UnreliableCar class.
    """
    my_car = UnreliableCar("Ford", 250, 50.5)

    # Try to drive the car multiple times because it is random.
    for i in range(5):
        print(f"{my_car.name} has driven {my_car.drive(50)}km.")
        print(my_car)


main()
