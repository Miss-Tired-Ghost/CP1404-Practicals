"""
Silver Service Taxi Implementation
Code By April First/Miss Ghost
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Define the SilverServiceTaxi class.
    Inherits from Taxi
    Implements flagfall cost to all fairs"""
    flagfall = 4.50  # $/fair

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def get_fare(self):
        """Determine the price of the taxi trip."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return string representation of the SilverServiceTaxi instance."""
        return (f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}")
