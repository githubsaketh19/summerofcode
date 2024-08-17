
value = int(input("Enter the value"))

def fizzBuzz(value):
    for number in range(1,value):
        if number % 3 == 0 and number % 5 == 0:
            print(number, ": FizzBuzz")
        elif number % 3 == 0:
            print(number, ": Fizz")
        elif number % 5 == 0:
            print(number, ": Buzz")
        else:
            print(number)

fizzBuzz(value)