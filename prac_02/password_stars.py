"""
Provide utility functions for obtaining and displaying passwords.
Code by: Miss Ghost/April First
"""
def main():
    minimum_length = 8
    password = get_password(minimum_length)
    print_censored_text(password)

def print_censored_text(text):
    print("*" * len(text))

def get_password(minimum_length):
    """Gets a password from a user, ensuring it has the minimum length."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print(f"Password must have at least {minimum_length} characters")
        password = input("Password: ")
    return password

if __name__ == "__main__":
    main()