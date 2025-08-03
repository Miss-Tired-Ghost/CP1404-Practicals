"""
Inheritance Example
Code By: April First/Miss Ghost
"""

from random import randrange
from prac_09.car import Car


class UnreliableCar(Car):
    """Define UnreliableCar object, inherits from Car"""
    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if random float is less than reliability.
        """
        if randrange(0, 100) < self.reliability:
            distance = super().drive(distance)
        else:
            distance = 0
        return distance
