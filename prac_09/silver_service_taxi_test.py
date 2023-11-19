"""
CP1404/CP5632 Practical
Program to test SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """
    Test to see if SilverServiceTaxi class calculates fares correctly.
    """

    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)

    bmw = SilverServiceTaxi("BMW", 250, 2)
    print(f"{bmw.name} has driven {bmw.drive(18)}km.")
    print(f"Current fare: ${bmw.get_fare()}")


main()
