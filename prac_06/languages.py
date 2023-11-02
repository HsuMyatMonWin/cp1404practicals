"""
languages.py

Estimated Time: 25 mins
Start Time: 8:02pm
Finish Time: 8:33pm
Actual Time: 31 mins
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

# programming_languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
#                          ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
#                          ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

programming_languages = [python, ruby, visual_basic]

for programming_language in programming_languages:
    if programming_language.is_dynamic():
        print(programming_language.name)
