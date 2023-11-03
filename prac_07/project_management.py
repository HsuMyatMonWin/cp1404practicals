"""
Project Management Program
CP1404 Practical 07 Exercise program file

Estimated Time: 1hour and 30mins
Start Time: 2:55pm
Break Time: 4:00pm - 4:25pm
Finish Time: 5:20pm
Actual Time: 2hours
"""
from project import Project
import datetime

FILE_NAME = "projects.txt"


def main():
    """
    Load a list of projects from a file. Display a menu to the user and allow the user to add, update, display
    and filter projects. Save the project list to a file when the user exit the program.
    """
    projects = load_projects(FILE_NAME)

    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
          "- (F)ilter projects by date\n- (A)dd new project\n"
          "- (U)pdate project\n- (Q)uit)")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name = input("Enter file name to load projects from: ")
            load_projects(file_name)
        elif choice == "S":
            file_name = input("Enter file name to save projects to: ")
            save_projects(projects, file_name)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "A":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice.")
        print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
              "- (F)ilter projects by date\n- (A)dd new project\n"
              "- (U)pdate project\n- (Q)uit)")
        choice = input(">>> ").upper()

    save_projects(projects, FILE_NAME)
    print("Thank you for using custom-built project management software.")


def load_projects(file_name):
    """
    Read project list from a file, store it in a list and return the list.

    :param file_name: string, the name of the project list file.
    :return: list
    """
    with open(file_name, 'r') as in_file:
        projects = []
        in_file.readline()
        for line in in_file:
            data = line.strip().split("\t")
            date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
            projects.append(Project(data[0], date, int(data[2]), float(data[3]), float(data[4])))
    return projects


def display_projects(projects):
    """
    Display the projects in two groups; incomplete projects; completed projects, both sorted by priority.

    :param projects: list, a list of projects.
    :return: None
    """
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

    incomplete_projects.sort()
    completed_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_project(projects):
    """
    Get a date from the user and display projects started after the specified date.

    :param projects: list, a list of projects.
    :return: None
    """
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = {}
    for project in projects:
        if project.start_date >= date:
            filtered_projects[project.start_date] = project
    for project in sorted(filtered_projects.items()):
        print(project[1])


def update_project(projects):
    """
    Display the project list, ask the user to choose a project, and then ask for new completion % and priority.
    Update the project details with these new values. Retain existing values when input is blank.

    :param projects: list, a list of projects.
    :return: None
    """
    for i, project in enumerate(projects, 0):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        is_finished = False
        while not is_finished:
            try:
                projects[choice].completion_percentage = float(new_percentage)
                is_finished = True
            except ValueError:
                print("Invalid input. Please try again!")

    new_priority = input("New Priority:")
    if new_priority != "":
        is_finished = False
        while not is_finished:
            try:
                projects[choice].priority = int(new_priority)
                is_finished = True
            except ValueError:
                print("Invalid input. Please try again!")


def add_project(projects):
    """
    Ask the name, start date, priority, cost estimate and completion percentage of a new project from a user
    and add a new project to the project list.

    :param projects: list, a list of projects.
    :return: None
    """
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = float(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def save_projects(projects, file_name):
    """
    Write the project list in the specified file.

    :param projects:
    :param file_name:
    :return: None
    """
    with open(file_name, 'w', newline='') as out_file:
        print("Name", "Start Date", "Priority", "Cost Estimate",
              "Completion Percentage", sep="\t", file=out_file)
        for project in projects:
            print(project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost_estimate,
                  project.completion_percentage, sep="\t", file=out_file)


if __name__ == '__main__':
    main()
