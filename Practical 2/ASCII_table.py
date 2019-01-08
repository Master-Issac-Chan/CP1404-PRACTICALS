LOWER = 33
UPPER = 127

characterConvert = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(characterConvert, ord(characterConvert)))
numberConvert = int(input("Enter a number between 33 and 127: "))
while numberConvert < LOWER or numberConvert > UPPER:
    print("Please enter a number only between 33 and 127")
    numberConvert = int(input("Enter a number between 33 and 127: "))
print("The character for {} is {}".format(numberConvert, chr(numberConvert)))
