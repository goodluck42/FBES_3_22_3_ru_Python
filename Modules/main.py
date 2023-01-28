# import my_math
import my_math as mm

from my_math import divide as dv, multiply as mult

# from my_math import *


def main():
    my_math = 42

    while True:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            # result = my_math.add(num1, num2)
            result = mm.add(num1, num2)

            print(result)
        elif op == "-":
            pass
        elif op == "*":
            result = mult(num1, num2)

            print(result)
        elif op == "/":
            result = dv(num1, num2)

            print(result)
        else:
            print("Incorrect operator")


if __name__ == "__main__":
    main()
