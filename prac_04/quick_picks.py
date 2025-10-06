import random

min = 1
max = 45
num_per_lines = 6

def main():
    num_quick_picks = int(input("How many quick picks?:"))

    for i in range(num_quick_picks):
        quick_picks = []
        for x in range(num_per_lines):
            number = random.randint(min, max)
            while number in quick_picks:
                number = random.randint(min, max)
            quick_picks.append(number)
            # need to format number
        print(" ".join(f"{number:2}" for number in quick_picks))

main()
