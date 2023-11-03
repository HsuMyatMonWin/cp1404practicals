"""
Project Management Program
CP1404 Practical 07 Exercise project module file

Estimated Time: 1hour and 30mins
Start Time: 2:55pm


"""
import datetime


class Project:
    """
    Represent a Project object.
    """

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initialise an instance of a Project.

        name: string, the name of the project.
        start_date: string, the starting date of a project.
        priority: integer, the project's priority.
        cost_estimate: float, the estimated cost of the project.
        completion_percentage: float, the completed percentage of the project.
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """
        Return the string representation of Project object.

        :return: str
        """
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage:.0f}%"


    def __lt__(self, other):
        """
        Compare two Project objects by priority.

        :param other: Project object, another Project instance to compare to.
        :return: bool
        """
        return self.priority < other.priority
