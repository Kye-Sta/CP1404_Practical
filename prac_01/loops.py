#a
print("a)")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#b
print("b)")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
numbers_of_stars = int(input("Enter the number of stars:"))
print("c)")
print("*" * numbers_of_stars)
print()

#d
print("d)")
lines = numbers_of_stars
for i in range(1, lines + 1):
    print("*" * i + " " * (lines - i))




