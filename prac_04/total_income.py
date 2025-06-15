"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    print("")  # to make output match sample

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    # removing the extra parameter feels very good
    # but recalculating the length feels bad
    # is there a better way I should be doing this? (genuine question)
    # my gut is telling me there isn't
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        # converted to fstring for readability
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()
