"""
Time Estimate: 30 min
Work Time: 90 min
Code by: Miss Ghost/April First
"""

import datetime
from operator import attrgetter
from project import Project

DEFAULT_FILE_NAME = 'projects.txt'
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE_NAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Enter new filename")
            load_projects(filename)
        elif choice == 'S':
            save_projects(DEFAULT_FILE_NAME, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            create_new_project(projects)
        elif choice == 'U':
            update_project(projects)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save = input("Would you like to save to projects.txt?").upper()
    if save == 'Y':
        save_projects(DEFAULT_FILE_NAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename) as file:
        file.readline()
        for line in file:
            parts = line.split("\t")
            name = parts[0]
            start = datetime.datetime.strptime(parts[1], "%d/%m/%Y")
            priority = int(parts[2])
            estimate = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(name, start.date(), priority, estimate, completion))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        print("Name	Start\tDate\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            print(f"{project.name}\t{project.start}\t{project.priority}\t"
                  f"{project.estimate:.2f}\t{project.completion:.2f}%", file=file)


def display_projects(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    complete_projects.sort(key=attrgetter("priority"))
    incomplete_projects.sort(key=attrgetter("priority"))

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Complete projects: ")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    start_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%y")
    filtered_projects = []
    for project in projects:
        if project.start > start_date.date():
            filtered_projects.append(project)
    display_projects(filtered_projects)


def create_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%y")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start.date(), priority, estimate, completion))


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    index = int(input("Project choice: "))
    print(projects[index])
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    try:
        new_percentage = int(new_percentage)
    except ValueError:
        new_percentage = ""
    try:
        new_priority = int(new_priority)
    except ValueError:
        new_priority = ""
    projects[index].update(new_percentage, new_priority)


if __name__ == '__main__':
    main()
