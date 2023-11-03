"""
Project Management Program
CP1404 Practical 07 Exercise program file

Estimated Time: 1hour and 30mins
Start Time: 2:55pm
Break Time: 4:00pm - 4:25pm
Finish Time: 5:40pm
Actual Time: 2hours and 20mins
"""


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

    def is_after(self, date):
        """
        Determine whether the project is after the specified date.

        :param date: datetime object, the date to determine if the project is started after or not.
        :return: bool
        """
        return self.start_date >= date
