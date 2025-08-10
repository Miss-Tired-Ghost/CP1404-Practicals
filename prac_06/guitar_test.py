"""
Test guitar class correctness
Goaltime: 15 min
Worktime: 22 min
Code by: Miss Ghost/April First
"""

from prac_06.guitar import Guitar


def main():
    """Create and test guitars"""
    index_to_expected = {"0": {"age": 103, "is_vintage": True},
                         "1": {"age": 15, "is_vintage": False},
                         "2": {"age": 12, "is_vintage": False}}

    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
               Guitar("Line 6 JTV-59", 2010, 1512.9),
               Guitar("Another Guitar", 2013, 0)]

    # get_age() tests
    is_incorrect = False
    for index, guitar in enumerate(guitars):
        if index_to_expected[str(index)]['age'] != guitar.get_age():
            is_incorrect = True
        print(f"{guitar.name} get_age() - "
              f"Expected {index_to_expected[str(index)]['age']}. "
              f"Got {guitar.get_age()}")
    if is_incorrect:
        print("WARNING : get_age() is incorrect.")

    # is_vintage() tests
    is_incorrect = False
    for index, guitar in enumerate(guitars):
        if index_to_expected[str(index)]['is_vintage'] != guitar.is_vintage():
            is_incorrect = True
        print(f"{guitar.name} get_age() - "
              f"Expected {index_to_expected[str(index)]['is_vintage']}. "
              f"Got {guitar.is_vintage()}")
    if is_incorrect:
        print("WARNING : is_vintage() is incorrect.")


if __name__ == '__main__':
    main()
