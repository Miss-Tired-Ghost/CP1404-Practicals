"""
Define guitar class
Goaltime: 15 min
Worktime: 7 min
Code by: Miss Ghost/April First
"""
import datetime


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the Guitar."""
        return datetime.date.today().year - self.year

    def is_vintage(self):
        """Returns True if Guitar is 50 or more years old."""
        return self.get_age() >= 50
