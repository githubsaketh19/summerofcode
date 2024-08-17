
number = int(input("Enter a number betweem 1 and 55296"))

def printAsciiTable():
    for i in range(1, number):
        print(i, chr(i))

printAsciiTable()