"""
Taxi Class utilisation example
Code By: April First/Miss Ghost
"""

from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"{my_taxi}\nCurrent Fare is: ${my_taxi.get_fare()}")

my_taxi.start_fare()
my_taxi.drive(100)
print(f"{my_taxi}\nCurrent Fare is: ${my_taxi.get_fare()}")






#
#
#
#
# Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
#
# Drive the taxi 40 km
#
# Print the taxi's details and the current fare
#
# Restart the meter (start a new fare) and then drive the car 100 km
#
# Print the details and the current fare