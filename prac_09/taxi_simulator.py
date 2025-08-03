"""
Taxi Simulator
Code By: April First/Miss Ghost
"""


from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """
    Define the main program loop

    Initialise bill, current taxi and taxis
    Display menu
    Get user input
    Loop
        Call functions based on user input (q, c, d, other)
        Display total bill
        Display menu
        Get user input
    """
    bill = 0.00
    current_taxi = None
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "d":
            bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        choice = input(">>> ").lower()


def drive_taxi(current_taxi):
    """Drive selected taxi, returns cost of trip"""
    if current_taxi:
        print("You need to choose a taxi before you can drive")
        return 0
    else:
        current_taxi.start_fare()
        distance = input("# Drive how far? ")
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
        return current_taxi.get_fare()


def choose_taxi(current_taxi, taxis):
    """Change selected taxi"""
    print("Taxis available:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")
    taxi_choice = input("Choose taxi: ")
    try:
        current_taxi = taxis[int(taxi_choice)]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


if __name__ == "__main__":
    main()
