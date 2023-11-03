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
    for project in projects:
        print(project)


def load_projects(file_name):
    """
    Read project list from a file and store it in a list.

    :param file_name: string, the name of the project list file.
    :return: list
    """
    with open(file_name, 'r') as in_file:
        projects = []
        in_file.readline()
        for line in in_file:
            data = line.strip().split("\t")
            projects.append(Project(*data))
    return projects


if __name__ == '__main__':
    main()
