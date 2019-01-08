from prac_8.unreliable_car import UnreliableCar
from random import randint

def main():
    unreliableCar = UnreliableCar("Unreliable", 100, randint(1.00,100.00))
    unreliableCar.drive(100)
    print(unreliableCar)