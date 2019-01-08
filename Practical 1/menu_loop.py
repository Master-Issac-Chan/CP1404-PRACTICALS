name = str(input("Enter name: "))
menuChoice = input(print("(H)ello\n(G)oodbye\n(Q)uit\n"))
while menuChoice != 'Q':
    if menuChoice == 'H' or menuChoice == 'h':
        print("Hello", name)
        menuChoice = input(print("(H)ello\n(G)oodbye\n(Q)uit\n"))
    elif menuChoice == 'G' or menuChoice == 'g':
        print("Goodbye", name)
        menuChoice = input(print("(H)ello\n(G)oodbye\n(Q)uit\n"))
    else:
        print("Invalid choice")
        menuChoice = input(print("(H)ello\n(G)oodbye\n(Q)uit\n"))
if menuChoice == 'Q':
    print("Finished")