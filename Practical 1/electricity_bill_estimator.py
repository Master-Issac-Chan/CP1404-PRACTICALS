TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def main():
    electricityUsed = int(input("Which tariff? 11 or 31: "))
    daysUsed = int(input("Please enter the amount of electricity used days: "))
    chargeRate = int(input("Please enter the price in cents: "))

    if electricityUsed == 11:
        electricityUsed = TARIFF_11
    elif electricityUsed == 31:
        electricityUsed = TARIFF_31

    totalElectricity = electricityUsed * daysUsed
    totalBill = (totalElectricity * chargeRate)/100

    print("Total billable amount for electricity use:", format(totalBill, '.2f'))

main()