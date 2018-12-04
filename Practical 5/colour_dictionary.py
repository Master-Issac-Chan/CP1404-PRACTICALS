COLOUR_NAMES = {"red": "#ff0000", "orange": "#ffa500", "yellow": "#ffff00", "green": "#00ff00", "blue": "#0000ff", "purple": "#a020f0", "pink": "#ffc0cb", "brown": "#a52a2a", "grey": "	#bebebe", "cyan": "#00ffff"}
# print(COLOUR_NAMES)

colour = input("Enter colour name: ")
while colour != "":
    colour = colour.lower()
    if colour in COLOUR_NAMES:
        print(colour, "colour code is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")