from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(fancy_taxi.get_fare())
    assert fancy_taxi.get_fare() == 48.80

main()