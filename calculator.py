def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def read_positive_integer(prompt):
    while True:
        value = int(input(prompt))
        if value > 0:
            return value
        print("Please enter a positive integer.")

if __name__ == "__main__":
    first = read_positive_integer("Enter the first positive integer: ")
    second = read_positive_integer("Enter the second positive integer: ")

    print(f"{first} + {second} = {add(first, second)}")
    print(f"{first} - {second} = {subtract(first, second)}")
    print(f"{first} * {second} = {multiply(first, second)}")
