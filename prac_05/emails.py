def main():
    email_collection = {}
    email = input("Enter an email: ")
    while email != "":
        name = get_name(email)
        correction_test = input(f"Is your name, {name}? (Y/n) ")
        if correction_test == "" or correction_test.lower() == "y":
            email_collection[email] = name
        else:
            name = input("Name: ")
            email_collection[email] = name

        email = input("Enter an email: ")
    print("Emails dictionary:")
    for email, name in email_collection.items():
        print(f"{name} ({email})")


def get_name(email):
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name


main()
