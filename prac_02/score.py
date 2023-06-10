"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():

    score = float(input("Enter score: "))
    score_rating = determine_score_rating(score)
    print(score_rating)

    random_score = randint(0, 100)
    random_result = determine_score_rating(random_score)
    print(random_score)
    print(random_result)

def determine_score_rating(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
