from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    bill_to_date = 0.0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    user_choice = ""
    while user_choice != "Q":
        print_menu(bill_to_date, taxis)
        user_choice = input(">>> ").upper()

        if user_choice == "C":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                trip_cost = drive_taxi(current_taxi, distance)
                bill_to_date += trip_cost
        elif user_choice != "Q":
            print("Invalid option")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)


def print_menu(bill_to_date, taxis):
    print("q)uit, c)hoose taxi, d)rive")
    print(f"Bill to date: ${bill_to_date:.2f}")
    print_taxis(taxis)


def print_taxis(taxis):
    print("Taxis available:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def choose_taxi(taxis):
    print_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    if 0 <= taxi_choice < len(taxis):
        return taxis[taxi_choice]
    else:
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi, distance, taxi_choice):
    if taxi_choice == 0:
        trip_cost = taxi.drive(distance) * taxi.get_fare() / 100  # Almost certain this not how this was supposed to be done.
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    else:
        trip_cost = taxi.drive(distance) * taxi.get_fare() / 100  # Unsure how to get this to refer to silver_service_taxi instead
    print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")  # of normal taxi fare
    return trip_cost


if __name__ == '__main__':
    main()
