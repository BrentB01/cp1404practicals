minimum_password_length = 10


def main():
    get_password()


def get_password():
    password = len(input("Enter a password: "))
    is_password_below_minimum_length(password)


def is_password_below_minimum_length(password):
    if password < minimum_password_length:
        print("Invalid password length.")
    else:
        print("*" * password)


main()


