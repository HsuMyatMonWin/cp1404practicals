"""
Project Management Program
CP1404 Practical 07 Exercise program file

Estimated Time: 1hour and 30mins
Start Time: 2:55pm


"""
from project import Project

FILE_NAME = "projects.txt"


def main():
    """
    doc string here
    """
    projects = load_projects(FILE_NAME)
    display_projects(projects)
    filter_project(projects)


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
            projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), float(data[4])))
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
    date = input("Show projects that start after date (dd/mm/yy): ")
    for project in projects:
        if project.start_date > date:
            print(project)


if __name__ == '__main__':
    main()
