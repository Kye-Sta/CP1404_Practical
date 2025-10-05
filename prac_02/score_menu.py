MENU = """(G)et a Valid Score
(P)rint Result
(S)how Stars
(Q)uit
"""
print(MENU)
def main():
    choice = input(">>>").upper()
    score = None

    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(score)
        elif choice == "P":
            if score is not None:
                result = determine_grade(score)
                print(result)
            else:
                print("Please enter score first")
        elif choice == "S":
            if score is not None:
                print_stars(score)
            else:
                print("Please enter score first")
        else:
            print("Invalid Option")
        print(MENU)
        choice = input(">>>").upper()


    # Prompt User for a score between 0 - 100
def get_score():
    score = int(input("Enter a Score between 0 - 100:"))
    while score < 0 or score > 100:
        print("Invalid Input")
        score = int(input("Enter a Valid Score:"))
    return score

def determine_grade(score):
    if score > 50:
        return "Passable"
    if score > 90:
        return "Excellent"
    else:
        return "Bad"

def print_stars(score):
    print("*" * score)

main()









