"""
Store users' emails and names in a dictionary
Goaltime: 15 min
Worktime: 13 min 03 sec
Code by: Miss Ghost/April First
"""


def main():
    """
    Get email and confirm name, storing into dictionary
    """
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = " ".join(part.title() for part in email.split("@")[0].split("."))
        correct_choice = input(f"Is your name {name}? (Y/n)").lower()
        if correct_choice == "y" or correct_choice == "":
            pass
        else:
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == '__main__':
    main()
