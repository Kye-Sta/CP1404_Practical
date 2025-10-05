Min_Length = 4

#main function
def main():
    password = get_password()
    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Enter Password:")
    while len(password) < Min_Length:
        password = input(f"Enter password with at least {Min_Length} character:")
    return password


#call function
main()