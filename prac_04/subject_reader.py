"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = get_data()
    display_subject_details(subject_details)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_details.append(parts)
    input_file.close()
    return subject_details


def display_subject_details(subject_details):
    for subject_detail in subject_details:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]:12} and has {subject_detail[2]:>3} students")


main()
