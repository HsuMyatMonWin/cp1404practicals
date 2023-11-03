"""
More Guitars Exercise for CP1404 Practical 7
Guitar file reader
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
    get_new_guitar(guitars)
    save_guitars(FILE_NAME, guitars)


def load_guitars(file_name):
    """
    Load guitar list from the specified csv file.

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


def get_new_guitar(guitars):
    """
    Get new guitars from the user and add to the list.

    :param guitars: list, a list of Guitar objects.
    """
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")


def save_guitars(file_name, guitars):
    """
    Write the guitar list to the specified csv file.

    :param file_name: string, the name of the csv file to save the guitar list.
    :param guitars: list, a list of Guitar objects.
    """
    out_file = open(file_name, 'w', newline='')
    writer = csv.writer(out_file)
    for guitar in guitars:
        writer.writerow((guitar.name, guitar.year, guitar.cost))
    out_file.close()


if __name__ == '__main__':
    main()
