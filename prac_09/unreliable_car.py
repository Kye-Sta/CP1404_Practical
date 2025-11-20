"""
CP1404/CP5632 Practical
Car class
"""
from random import randint

from prac_09.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        ran_int = randint(1,100)
        if ran_int >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven > 0
