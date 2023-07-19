name = input("Enter your name: ")
choice = ""

while choice != "Q":
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input("Enter your choice: ")

    if choice == "H":
        print("Hello,", name)
    elif choice == "G":
        print("Goodbye,", name)
    elif choice == "Q":
        break
    else:
        print("Invalid choice")

print("Finished.")
