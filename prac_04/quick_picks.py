import random

MINIMUM_LIMIT = 1
MAXIMUM_LIMIT = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    generate_quick_picks(number_of_quick_picks)


def generate_quick_picks(number_of_quick_picks):
    for number in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(str(number) for number in quick_pick))


def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MINIMUM_LIMIT, MAXIMUM_LIMIT)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()








