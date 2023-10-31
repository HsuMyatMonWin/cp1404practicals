"""
Emails
Estimate: 25 minutes
Actual:   26 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice != "Y" and choice != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """ Extracts name from an email address """
    name = " ".join(email.split(sep="@")[0].split(".")).title()
    return name


main()
