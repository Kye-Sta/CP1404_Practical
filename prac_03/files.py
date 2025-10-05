FILENAME = "name.txt"

def write_name():
    #open file
    open_file = open(FILENAME, 'w')
    #process file
    name = input("Enter your name:")
    print(name, file=open_file)
    #close file
    open_file.close()

def read_name():
    in_file = open(FILENAME, 'r')
    name = in_file.read().strip()
    in_file.close()
    print(f"Hello {name}")

def calculate_number():
    with open("numbers.txt", 'r') as in_file:
        number_one = int(in_file.readline())
        number_two = int(in_file.readline())
        result = number_one + number_two
    print(result)

def read_file():
    total = 0
    with open("numbers.txt", 'r') as in_file:
        for line in in_file:
            total += int(line)
        print(total)

write_name()
read_name()
calculate_number()
read_file()
