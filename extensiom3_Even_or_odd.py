
evenOrOdd = int(input("Enter a number to check if it is even or odd"))

def isOdd(number):
    return number % 2 == 1
    print("Your number ", evenOrOdd, " is odd")

def isEven(number):
    return  number % 2 == 0
    print("Your number ", evenOrOdd, " is even")


if evenOrOdd % 2 == 1:
    value1 = isOdd(evenOrOdd)
    print(value1)
elif evenOrOdd % 2 == 0:
    value2 = isEven(evenOrOdd)
    print(value2)