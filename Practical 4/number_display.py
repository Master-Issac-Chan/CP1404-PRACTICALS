numbers = []
number_count = 0
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
    number_count += 1

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(float(sum(numbers)/number_count)))