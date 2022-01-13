
def add(x, y):
    sum = x + y
    return sum


def subtract(x, y):
    sum = x-y
    return sum


def divide(x, y):
    sum = x / y
    return sum


def multiply(x, y):
    sum = x * y
    return sum

sum = 0

Options = [add.__name__, subtract.__name__, divide.__name__, multiply.__name__]

for i in range(len(Options)):
    print(Options[i])

Selection = input("Type selection from options above or exit ")

while Selection != "exit":

    if Selection == "add":
        num1 = int(input("Select a number "))
        if sum !=0:
            print(f"{sum} + {num1} = {add(sum, num1)}")
            sum =add(sum, num1)
        else:    
            num2 = int(input("Select second number "))
            sum = add(num1, num2)
            print(f"{num1} + {num2} = {sum}")


    elif Selection == "subtract":
        num1 = int(input("Select a number "))
        if sum != 0:
            print(f"{sum} - {num1} = {subtract(sum, num1)}")
            sum = subtract(sum, num1)
        else:            
            num2 = int(input("Select second number "))
            sum = subtract(num1, num2)
            print(f" {num1} - {num2} = {sum} ")


    elif Selection == "divide":
        num1 = int(input("Select a number "))
        if sum != 0:
            print(f"{sum} / {num1} = {divide(sum, num1)}")
            sum = divide(sum, num1)
        else:
            num2 = int(input("Select second number "))
            sum = divide(num1, num2)
            print(f"{num1} / {num2} = {sum}")

    elif Selection == "multiply":
        num1 = int(input("Select a number "))
        if sum != 0:
            print(f"{sum} + {num1} = {multiply(sum, num1)}")
            sum = multiply(sum, num1)
        else:    
            num2 = int(input("Select second number "))
            sum = multiply(num1, num2)
            print(f"{num1} * {num2} = {sum} ")

    print("x" * 30)
    for i in range(len(Options)):
        print(Options[i])
    print("Your current sum is:", sum)
    Selection = input("Type selection from options above or exit ")
