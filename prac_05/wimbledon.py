"""
Wimbledon
Estimate: 45 minutes
Actual:   48 minutes
"""

import csv


FILE_NAME = "wimbledon.csv"


def main():
    wimbledon_champions = load_data(FILE_NAME)
    display_champions(wimbledon_champions)
    print("")
    display_winning_countries(wimbledon_champions)


def display_winning_countries(wimbledon_champions):
    """ Display the name of countries that have won in Wimbledon. """
    winning_countries = set([country[3] for country in wimbledon_champions])

    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


def display_champions(wimbledon_champions):
    """ Display champion names and their winning counts. """
    champion_to_winning_count = {}
    for record in wimbledon_champions:
        if record[2] in champion_to_winning_count:
            champion_to_winning_count[record[2]] += 1
        else:
            champion_to_winning_count[record[2]] = 1

    for champion, winning_count in champion_to_winning_count.items():
        print(f"{champion} {winning_count}")


def load_data(file_name):
    """ Read data from the csv file. """
    wimbledon_champions = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file, delimiter=",")
        next(reader)  # removes header
        for record in reader:
            wimbledon_champions.append(record)
    return wimbledon_champions


main()
