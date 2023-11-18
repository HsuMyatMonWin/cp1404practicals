"""
Band class with Hsu and Gayle
"""


class Band:
    """Band class"""
    def __init__(self, name=""):
        """Construct a band with a name and empty list of musicians"""
        self.name = name
        self.musicians = []

    def __repr__(self):
        """Return a string representation of a band using a list comprehension"""
        return f"{self.name} ({','.join([str(musician) for musician in self.musicians])})"

    def add(self, musician):
        """Add a musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their instrument"""
        return '\n'.join([musician.play() for musician in self.musicians])

