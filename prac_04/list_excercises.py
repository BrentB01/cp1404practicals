def main():
    numbers = get_numbers()
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average = sum(numbers) / len(numbers)
    print_information(first_number, last_number, smallest_number, largest_number, average)
    # Woefully inadequate security checker (Didn't want to refactor this as it could get confusing)
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter your username :")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def get_numbers():
    numbers = []
    for number in range(0,5):
        number = float(input("Number: "))
        numbers.append(number)
    return numbers


def print_information(first_number, last_number, smallest_number, largest_number, average):
    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average}")


main()
