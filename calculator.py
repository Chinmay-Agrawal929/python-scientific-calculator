import math
def calculator():
    while True:
        print("-----SCIENTIFIC CALCULATOR-----", "1. Basic Arithematic(+, -, *, /)", "2. Power(x^y)", "3. Square Root(√x)", "4. Trigonometric Functions(sin(), cos(), tan(), cot(), sec(), csc())", "5. Logarithm(log(x))", "6. Factorial(x!)", "0. Exit", sep="\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            n1 = float(input("Enter first number: "))
            n2  = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")

            if op == '+':
                print(n1 + n2)
            elif op == '-':
                print(n1 - n2)
            elif op == '*':
                print(n1 * n2)
            elif op == '/':
                if n2 != 0:
                    print(n1 / n2)
                else:
                    print("Error: Division by zero")
            else:
                print("Invalid operator")

        elif choice == '2':
            base = float(input("Enter the base number: "))
            exponent = float(input("Enter the exponent: "))
            print(math.pow(base, exponent))

        elif choice == '3':
            n = float(input("Enter the number to find the Square Root: "))
            if n >= 0:
                print(math.sqrt(n))
            else:
                print("Error: Cannot compute square root of negative number(-ve)")

        elif choice == '4':
            function = input("Enter a function (sin(), cos(), tan(), cot(), sec(), csc()): ")
            angle = float(input("Enter the angle: "))
            if function == "sin()":
                print(math.sin(math.radians(angle)))
            elif function == "cos()":
                print(math.cos(math.radians(angle)))
            elif function == "tan()":
                print(math.tan(math.radians(angle)))
            elif function == "cot()":
                tan_val = math.tan(math.radians(angle))
                if tan_val != 0:
                    print(1 / tan_val)
                else:
                    print("Error: Undefined (division by zero)")
            elif function == "sec()":
                cos_val = math.cos(math.radians(angle))
                if cos_val != 0:
                    print(1 / cos_val)
                else:
                    print("Error: Undefined (division by zero)")
            elif function == "csc()":
                sin_val = math.sin(math.radians(angle))
                if sin_val != 0:
                    print(1 / sin_val)
                else:
                    print("Error: Undefined (division by zero)")
            else:
                print("Error: Invalid function")

        elif choice == '5':
            n = float(input("Enter the number to find the Logarithms: "))
            if n > 0:
                print(math.log(n))
            else:
                print("Error: Cannot compute logarithm of non-positive number")

        elif choice == '6':
            n = int(input("Enter the number to find the factorial: "))
            if n >= 0:
                print(math.factorial(n))
            else:
                print("Error: Cannot compute factorial of negative number")

        elif choice == '0':
            print("Exiting the calculator.", "Goodbye! And have a nice day!", sep="\n")
            break

        else:
            print("Error: Invalid choice. Please try again.")

calculator()