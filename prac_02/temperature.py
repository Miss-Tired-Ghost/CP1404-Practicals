"""
Provides utility functions for converting Celsius to Fahrenheit and vice versa.
Code by: Miss Ghost/April First
"""
def main():
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit
    """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        match choice:
            case "C":
                celsius = float(input("Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"Result: {fahrenheit:.2f} F")

            case "F":
                fahrenheit = float(input("Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"Result: {celsius:.2f} C")

            case _:
                print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

if __name__ == "__main__":
    main()