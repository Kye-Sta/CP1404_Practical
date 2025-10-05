"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))

def determine_grade(score):
    if score >= 0:
        if score > 100:
            return "Invalid score"
        if score > 50:
            return "Passable"
        if score > 90:
            return "Excellent"
        else:
            return "Bad"
    else:
        return "Invalid Score"



main()