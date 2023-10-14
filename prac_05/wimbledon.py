"""
Wimbledon
Estimate: 45 minutes
Actual:   48 minutes
"""

import csv


def main():
    file_name = "wimbledon.csv"
    wimbledon_champions = load_data(file_name)
    display_champions_and_winning_counts(wimbledon_champions)
    print("")
    display_winning_countries(wimbledon_champions)


def display_winning_countries(wimbledon_champions):
    winning_countries = set([country[3] for country in wimbledon_champions])

    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


def display_champions_and_winning_counts(wimbledon_champions):
    champion_to_winning_count = {}
    for record in wimbledon_champions:
        if record[2] in champion_to_winning_count:
            champion_to_winning_count[record[2]] += 1
        else:
            champion_to_winning_count[record[2]] = 1

    for champion, winning_count in champion_to_winning_count.items():
        print(f"{champion} {winning_count}")


def load_data(file_name):
    wimbledon_champions = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file, delimiter=",")
        next(reader)  # removes header
        for record in reader:
            wimbledon_champions.append(record)
    return wimbledon_champions


main()
