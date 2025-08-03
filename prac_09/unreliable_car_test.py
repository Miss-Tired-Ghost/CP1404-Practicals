"""
Testing for Unreliable Car Class
Code By: April First/Miss Ghost
"""

from prac_09.unreliable_car import UnreliableCar

# Initialise testing variables
test_car = UnreliableCar("AMC Gremlin", 100, 30)
number_of_successful_drives = 0

# Test Loop
for _ in range(1000):
    # Reset Test Car
    test_car.fuel = 100
    test_car.odometer = 0

    # Run Test
    test_car.drive(50)
    if test_car.odometer == 50:
        number_of_successful_drives += 1

# Evaluate Results
print(number_of_successful_drives)
if 250 < number_of_successful_drives < 350:
    print("Probably Working")
else:
    print("Probably Not Working")
