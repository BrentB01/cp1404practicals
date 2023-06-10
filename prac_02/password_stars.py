password = len(input("Enter a password: "))
minimum_password_length = 10
if password < minimum_password_length:
    print("Invalid password length.")
else:
    print("*" * password)
