
Min_Password_Len = 4
password = input("Enter Password:")
while len(password) < Min_Password_Len:
    print("Invalid Length of Password")
    password = input("Enter Password:")

print("*" * len(password))
