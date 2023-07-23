class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) - ${self.cost:.2f}"

    def __lt__(self, other):
        # Define how to compare guitars based on their year attribute
        return self.year < other.year


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are guitar data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    # Sort the list by year (oldest to newest)
    guitars.sort()
    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)

    name = input("Enter the name of the guitar (or 'exit' to stop): ")
    while name != "":
        if name.lower() == 'exit':
            break
        year = input("Enter the year of manufacture: ")
        cost = input("Enter the cost of the guitar: ")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Enter the name of the guitar (or leave blank to stop): ")
        # Open the file for writing (this will overwrite the existing data)
    out_file = open('guitars.csv', 'w')
    # Write the header
    out_file.write("Name,Year,Cost\n")
    # Write each guitar's data to the file
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    # Close the file after writing
    out_file.close()

    print("Data has been updated and saved to guitars.csv.")


if __name__ == "__main__":
    main()
