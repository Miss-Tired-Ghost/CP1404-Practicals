"""
Display wimbledon tennis championship information
Goaltime: 50 min
Worktime: 32 min 18 sec
Code by: Miss Ghost/April First
"""


FILENAME = 'wimbledon.csv'


def read_csv(filename):
    """
    Parse csv formatted file
    """
    records = []
    with open(filename, "r", encoding="utf-8-sig") as csv_file:
        csv_file.readline()  # remove headers
        for line in csv_file.readlines():
            records.append(line.split(","))
    return records


def tally_wins(records):
    """
    Count number of wins a champion has returning as a dictionary
    """
    champion_to_win_count = {}
    for record in records:
        champion_to_win_count[record[2]] = champion_to_win_count.get(record[2], 0) + 1
    return champion_to_win_count


def get_winning_countries(records):
    """
    Return all countries that have won as an alphabetical list
    """
    countries = set()
    for record in records:
        countries.add(str(record[1]))
    return sorted(list(countries))


def main():
    """Display results of the wimbledon championship"""
    records = read_csv(FILENAME)
    champion_to_win_count = tally_wins(records)
    print("Wimbledon Champions:")
    for champion, count in champion_to_win_count.items():
        print(champion, count)
    winning_countries = get_winning_countries(records)
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon: ")
    print(", ".join(winning_countries))


if __name__ == '__main__':
    main()
