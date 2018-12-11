"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    # my_car = Car(180) (fuel) is passed into my_car argument
    # my_car.drive(30) (distance) is passed into my_car.drive argument
    limo = Car(100, "Limo") #initialise limo & (fuel) is passed into limo argument
    limo.add_fuel(20) #added 20 more to fuel
    print("fuel =", limo.fuel)
    limo.drive(115) #(distance) is passed into limo.drive argument
    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))


main()