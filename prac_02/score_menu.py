
def get_valid_score():
    score = float(input("Enter score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score.")
    return score


def main():
    score = get_valid_score()
    choice = None

    while choice != "Q":
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            determine_score_rating(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Finished.")
        else:
            print("Invalid choice")

    print("Farewell.")


def determine_score_rating(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("Excellent")


def show_stars(score):
    print("*" * int(score))


main()
