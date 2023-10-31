"""
programming_language module

Estimated Time: 25 mins
Start Time: 8:02pm
Finish Time: 8:33pm
Actual Time: 31 mins
"""


class ProgrammingLanguage:
    """
    Represent a ProgrammingLanguage object.
    """

    def __init__(self, name, typing, reflection, year):
        """
        Inatialise a ProgrammingLanguage instance.

        name: string, name of the programming language
        typing: string, whether the language is dynamic typing or static typing
        reflection: boolean, whether the language supports reflection
        year: integer, the year the language was released
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """
        Determine whether the programming language is dynamic typing or not.

        :return: bool
        """
        return self.typing.upper() == "DYNAMIC"

    def __str__(self):
        """
        Return the name, typing, reflection and released year of the ProgrammingLanguage in a sentence.

        :return: str
        """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
