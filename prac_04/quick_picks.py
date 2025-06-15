"""
Generate a "Quick Pick" Lottery Ticket
Code by: Miss Ghost/April First
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = get_natural_number("How many quick picks? ")
    for _ in range(0, number_of_quick_picks):
        # disallowed version
        # picks = random.sample(range(MINIMUM, MAXIMUM), NUMBERS_PER_LINE)
        # picks.sort()

        # v1 presorted - likely fastest - biases large numbers
        # picks = []
        # current_minimum = MINIMUM
        # for i in range(0, NUMBERS_PER_LINE):
        #     current_maximum = MAXIMUM - NUMBERS_PER_LINE + i + 1
        #     picks.append(random.randint(current_minimum, current_maximum))
        #     current_minimum = picks[i]

        # v2 uses the property that a set cannot have duplicates
        picks = set()
        while len(picks) < NUMBERS_PER_LINE:
            picks.add(random.randint(MINIMUM, MAXIMUM))
        picks = sorted(picks)

        print(" ".join(f"{number:2}" for number in picks))


def is_valid_natural_number(query):
    try:
        number = float(query)
    except ValueError:
        print("Please enter a number.")
        return False
    if not number.is_integer():
        print("Number should be an integer.")
        return False
    if number < 1:
        print("Number should be at least 1.")
        return False
    return True


def get_natural_number(prompt="Enter a natural number"):
    """Get a natural number from the user, performing error handling until correct"""
    number = input(prompt)
    while not is_valid_natural_number(number):
        number = input(prompt)
    return int(number)


if __name__ == '__main__':
    main()
