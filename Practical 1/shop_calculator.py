def main():
    num = int(input("Enter the number of items purchasing: "))
    while (num <= 0):
        print("Invalid input")
        num = input("Please enter the number of items purchasing: ")

    total = 0.0
    for i in range(1, num+1, 1):
        price = float(input("Enter price for item: $"))
        print("Price: $", price)
        total += price
        print("Total: $", total)

    if (total >= 100.0):
        total = total * 0.9
    print("Total price of all items purchased: $", total)

main()