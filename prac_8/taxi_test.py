from prac_8.taxi import Taxi

def main():
    taxi1 = Taxi("Prius", 100)

    taxi1.drive(40)
    print(taxi1)
    print("The current fare is ${}".format(taxi1.get_fare()))
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1)
    print("The current fare is ${}".format(taxi1.get_fare()))

main()