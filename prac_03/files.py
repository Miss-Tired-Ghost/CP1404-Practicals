"""
Perform multiple small tasks with python's file methods
Code by: Miss Ghost/April First
"""
def main():
    name = input("What is your name? ")
    output_file = open("name.txt", "w")
    output_file.write(name)
    output_file.close()


    input_file = open("name.txt", "r")
    name = input_file.read()
    input_file.close()
    print(f"Hi {name}!")


    with open("numbers.txt", "r") as input_file:
        number_1 = int(input_file.readline())
        number_2 = int(input_file.readline())
        print(number_1 + number_2)


    with open("numbers.txt", "r") as input_file:
        total = 0
        for number in input_file:
            total += int(number)
        print(total)

if __name__ == "__main__":
    main()
