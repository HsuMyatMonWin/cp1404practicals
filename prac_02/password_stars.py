MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    print("Password set.")
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be {MINIMUM_LENGTH} characters long.")
        password = input("Enter password: ")
    return password


main()
