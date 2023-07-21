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


main()