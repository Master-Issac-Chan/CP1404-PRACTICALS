startNum = int(input("Please enter a starting low number: "))
endNum = int(input("Please enter an ending high number: "))

while startNum > endNum:
    print("Please input a lower number first and a higher number last")
    startNum = int(input("Please enter a starting low number: "))
    endNum = int(input("Please enter an ending high number: "))

print("Even numbers: ")
for i in range(startNum, endNum):
    if i % 2 == 0:
        print(i)

print("\nOdd numbers: ")
for j in range(startNum, endNum):
    if j % 2 > 0:
        print(j)


print("\nNumbers squared: ")
for k in range(startNum, endNum):
    k = k*k
    print(k)

quit()

