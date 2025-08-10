""""
Display usage of the Guitar custom class
Code by: Miss Ghost/April First
"""
import csv

from prac_07.guitar import Guitar


def main():
    """Read guitars.csv and store them in a list of Guitar objects, using the Guitar class"""
    guitars = create_guitars_from_csv()
    guitars.sort(reverse=True)

    # attrgetter version
    # guitars.sort(key=attrgetter('year', 'cost'))

    display_guitars(guitars)


def display_guitars(guitars):
    """Display a list of Guitar objects"""
    for guitar in guitars:
        print(guitar)


def create_guitars_from_csv():
    """Create a list of Guitar objects from a CSV file"""
    guitars = []
    with open('guitars.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            name = row[0]
            year = int(row[1])
            cost = float(row[2])

            guitars.append(Guitar(name, year, cost))
    return guitars


if __name__ == '__main__':
    main()
