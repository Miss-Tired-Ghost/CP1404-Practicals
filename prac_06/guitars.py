"""
Demonstrate guitar class utilisation
Goaltime: 15 min
Worktime: 22 min
Code by: Miss Ghost/April First
"""

from prac_06.guitar import Guitar


def add_test_guitars(guitars):
    """Initialise guitars for testing"""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Another Guitar", 2013, 0))


def get_guitars(guitars):
    """Create new guitar instances from user input."""
    print("My Guitars!")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")


def display_guitars(guitars):
    """Display guitars."""
    print("These are my guitars:")
    for index, guitar in enumerate(guitars):
        print(f"Guitar {index + 1}: {guitar.name:>20} ({guitar.year}), "
              f"worth $ {guitar.cost:,.2f} {"(vintage)" if guitar.is_vintage() else ""}")


def main():
    """Handle program execution."""
    guitars = []
    add_test_guitars(guitars)
    # get_guitars(guitars)
    display_guitars(guitars)


if __name__ == "__main__":
    main()
