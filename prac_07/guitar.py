"""
Modified Guitar module for Practical 7
Custom Guitar class
"""


class Guitar:
    """
    Represent a Guitar object.
    """

    def __init__(self, name="", year=0, cost=0):
        """
        Initialise a Guitar instance.
        :param name: string, the name of the guitar, default = ""
        :param year: integer, the year the guitar was made, default = 0
        :param cost: float, the price of the guitar, default = 0
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """
        Return the name, year and cost of the guitar in a sentence.
        :return: str
        """
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """
        Compare two Guitar instances by year.
        :param other: Guitar object, another guitar to compare with.
        :return: bool
        """
        return self.year < other.year

    def get_age(self, current_year):
        """
        Return how old the guitar is in years.
        :param current_year: integer, the current year
        :return: int
        """
        return current_year - self.year

    def is_vintage(self, current_year):
        """
        Determine whether the guitar is vintage or not.
        :param current_year: integer, the current year
        :return: bool
        """
        return self.get_age(current_year) >= 50
