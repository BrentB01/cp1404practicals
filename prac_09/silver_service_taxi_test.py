from silver_service_taxi import SilverServiceTaxi


def test_calculate_fare():
    # Create a SilverServiceTaxi with fanciness 2 and 18 km trip
    taxi = SilverServiceTaxi("Hummer", fuel=200, fanciness=2)

    taxi.drive(18)

    fare = taxi.get_fare()

    expected_fare = 48.80

    if fare == expected_fare:
        print(f"Expected fare: {expected_fare}, Actual fair: {fare}")
        print("All tests passed!")
    else:
        print(f'Tests failed (f"Expected fare: {fare}, Actual fair: {expected_fare}')


if __name__ == '__main__':
    test_calculate_fare()

