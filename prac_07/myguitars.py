"""
Read the details of guitars from a file and store them in a list of objects of custom Guitar class.
"""
import csv
from guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    """
    Read the guitar list for a file and display the guitars sorted by year.
    """
    guitars = load_guitars(FILE_NAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(file_name):
    """
    Load guitar list for the specified csv file.

    :param file_name: string, the name of the csv file that contains the guitar list.

    :return: list
    """
    guitars = []
    in_file = open(file_name, 'r', newline='')
    reader = csv.reader(in_file)
    for row in reader:
        year = int(row[1])  # convert year to integer type
        cost = float(row[2])  # convert cost to float type
        guitars.append(Guitar(row[0], year, cost))
    in_file.close()

    return guitars


if __name__ == '__main__':
    main()
