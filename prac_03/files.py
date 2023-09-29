# Program 1
file_name = "name.txt"
name = input("Enter your name: ")
out_file = open(file_name, "w")
print(name, file=out_file)
out_file.close()

# Program 2
file_name = "name.txt"
in_file = open(file_name, "r")
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()

# Program 3
file_name = "numbers.txt"
in_file = open(file_name, "r")
number_1 = int(in_file.readline().strip())
number_2 = int(in_file.readline().strip())
print(f"Result: {number_1 + number_2}")
in_file.close()

# Program 4
file_name = "numbers.txt"
total = 0
in_file = open(file_name, "r")
for line in in_file:
    total += int(line.strip())
print(f"Total: {total}")
in_file.close()
