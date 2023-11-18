"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that does not drive sometimes."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()} is only {self.reliability}% reliable"

    def drive(self, distance):
        """Drive like parent Car but only if it passes the reliable check."""
        distance_driven = 0
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
