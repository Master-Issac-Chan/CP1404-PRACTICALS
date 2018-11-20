"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 and score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("High Distinction")
    elif score >= 80:
        print("Distinction")
    elif score >= 70:
        print("Merit")
    elif score >= 60:
        print("Credit")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")