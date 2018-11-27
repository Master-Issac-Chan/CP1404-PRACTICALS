import random


quickPick = int(input("How many quick picks?: "))
for i in range(quickPick):
    pickList = []
    for j in range(6):
        pick = random.randrange(46) #pick random numbers for the 6
        while pick in pickList:
            pick = random.randrange(46)
        pickList.append(pick)
        if j == 5:
            pickList.sort()
            print(pickList)

