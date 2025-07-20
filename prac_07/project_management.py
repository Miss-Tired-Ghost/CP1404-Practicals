"""
Time Estimate: 30 min
Work Time
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
- (Q)uit
"""


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
            projects = filter_projects_by_date(projects)
        elif choice == 'A':
            projects.append(create_new_project())
        elif choice == 'U':
            update_project(projects)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


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
            projects.append(Project(name, start, priority, estimate, completion))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        print("Name	Start\tDate\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            print(
                f"{project.name}\t{project.start}\t{project.priority}\t{project.estimate:.2f}\t{project.completion:.2f}%",
                file=file)


def display_projects(projects):
    for project in projects:
        print(f"{project}")


def filter_projects_by_date(projects):
    projects.sort(attrgetter('start'), reverse=True)
    display_projects(projects)


def create_new_project():
    name = input("name")
    start = input("start")
    priority = int(input("priority"))
    estimate = float(input("estimate"))
    completion = int(input("completion"))
    return Project(name, start, priority, estimate, completion)


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    index = int(input("Project choice: "))
    print(projects[index])
    new_percentage = input("New Percentage: ")
    projects[index].update(new_percentage)


if __name__ == '__main__':
    main()
