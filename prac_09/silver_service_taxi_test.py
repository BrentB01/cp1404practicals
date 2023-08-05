from silver_service_taxi import SilverServiceTaxi


def test_calculate_fare():
    # Create a SilverServiceTaxi with fanciness 2 and 18 km trip
    taxi = SilverServiceTaxi("Hummer", fuel=200, fanciness=2)

    taxi.drive(18)

    fare = taxi.get_fare()

    expected_fare = 48.78

    if fare == expected_fare:
        print("All tests passed!")


if __name__ == '__main__':
    test_calculate_fare()

