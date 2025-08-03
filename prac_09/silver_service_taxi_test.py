""""
Tests for Silver Service Taxi class
Code By: April First/Miss Ghost
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


test_taxi = SilverServiceTaxi("Beetle", 200, 2)
test_taxi.drive(18)

assert test_taxi.__str__() == "Beetle, fuel=182, odo=18, 18km on current fare, $2.46/km plus flagfall of $4.50"
assert test_taxi.get_fare() == 48.80


test_taxi = SilverServiceTaxi("Hummer", 200, 4)
test_taxi.drive(44)

assert test_taxi.__str__() == "Hummer, fuel=156, odo=44, 44km on current fare, $4.92/km plus flagfall of $4.50"
assert test_taxi.get_fare() == 221.00

print("Tests passed")
