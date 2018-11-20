def main():
    electricityUsed = int(input("Please enter the amount of electricity used in kWh:"))
    daysUsed = int(input("Please enter the amount of electricity used days:"))
    chargeRate = int(input("Please enter the price in cents:"))

    totalElectricity = electricityUsed * daysUsed
    totalBill = (totalElectricity * chargeRate)/100

    print("Total billable amount for electricity use:", totalBill)

main()