"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    for subject in data:
        display_subject_details(*subject)


def display_subject_details(subject, lecturer, number_of_students):
    print(f"{subject} is taught by {lecturer:12} and has {number_of_students:3} students.")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")

        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])

        data.append(parts)
    input_file.close()
    return data


if __name__ == "__main__":
    main()
