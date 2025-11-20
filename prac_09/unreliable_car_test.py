from prac_09.unreliable_car import UnreliableCar


def main():

    car90 = UnreliableCar("Reliable", 100, 90)
    car10 = UnreliableCar("Unreliable", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{car90.name:12} drove {i}km: {car90.drive(i)}")
        print(f"{car10.name:12} drove {i}km: {car10.drive(i)}")
    print(car90)
    print(car10)


main()