value = int(input("Enter the number"))

def ordinalSuffix(value):
    for number in range(1, value):
        number = str(number)
        if number.endswith("11"):
            print(number,"th")
        if number.endswith("12"):
            print(number,"th")
        if number.endswith("13"):
            print(number,"th")
        if number.endswith("1"):
            print(number,"st")
        elif number.endswith("2"):
            print(number,"nd")
        elif number.endswith("3"):
            print(number,"rd")
        else:
            print(number,"th")

ordinalSuffix(value)
