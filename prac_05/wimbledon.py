import csv


def main():
    def read_csv(filename):
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            reader = csv.reader(in_file)
            next(reader)  # Skip the header row
            data = [row for row in reader]
        return data

    def count_wins(data):
        champions = {}
        for row in data:
            player = row[2]
            if player in champions:
                champions[player] += 1
            else:
                champions[player] = 1
        return champions

    def get_countries(data):
        countries = set()
        for row in data:
            country = row[3]
            countries.add(country)
        return sorted(countries)

    def display_champions(champions):
        print("Wimbledon Champions:")
        for player, wins in champions.items():
            print(f"{player} {wins}")

    def display_countries(countries):
        print("\nThese", len(countries), "countries have won Wimbledon:")
        country_string = ", ".join(countries)
        print(country_string)

    data = read_csv("wimbledon.csv")
    champions = count_wins(data)
    display_champions(champions)
    countries = get_countries(data)
    display_countries(countries)


main()
