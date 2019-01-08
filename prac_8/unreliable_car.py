from prac_8.car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, fuel, name, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        drivable_distance = super().drive(distance)(1.00, 100.00)
        if self.distance < self.reliability:
            drivable_distance = super().drive(distance)
            return drivable_distance
        else:
            self.distance = 0
            return drivable_distance

    def __str__(self):
        return ("{}, {}km on current reliability".format(super().__str__(), self.reliability))