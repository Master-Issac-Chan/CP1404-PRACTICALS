out_file = open("name.txt", 'w')
name = input("What is your name? ")
print(name, file = out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()


numbers_file = open("numbers.txt", "r")
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
print(number1 + number2)
numbers_file.close()
