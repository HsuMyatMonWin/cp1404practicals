"""
guitars.py

Estimated Time: 45 mins
Start Time: 9:02pm
Finish Time: 9:55pm
Actual Time: 53 mins
"""
from prac_06.guitar import Guitar

guitars = []
CURRENT_YEAR = 2022

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(f"{guitar} added.")
    guitars.append(guitar)
    name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
          f"worth ${guitar.cost:10,.2f}"
          f"{vintage_string}")
