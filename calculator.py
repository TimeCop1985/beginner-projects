import math


def calculator():

#  Addition
    def add(x, y):
        return x + y

    #   Subtraction
    def subtract(x, y):
        return x - y

    #   Multiplication
    def multiply(x, y):
        return x * y

    #   Division
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot Divide by Zero"

    #   Percentage
    def percentage(x, y):
        if y != 0:
            return x / y * 100
        else:
            return "Cannot Calculate Percentage with Zero Denominator"

    #   Power
    def power(x, y):
        if y == 0:
            return 1
        else:
            return x ** y

    #   Square Root
    def square_root(x):
        if x == 0:
            return "Invalid Number."
        else:
            return math.sqrt(x)

    #   Modulus
    def modulus(x, y):
        if y != 0:
            return x % y
        else:
            return "Cannot perform modulus with zero denominator"

    #   Get valid numbers
    def get_valid_numbers(prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print("Invalid Input. Please enter a number")

    def get_valid_nonzero_number(prompt):
        while True:
            try:
                number = float(input(prompt))
                if number != 0:
                    return number
                else:
                    print("Invalid Input. Please enter a non-zero number.")
            except ValueError:
                print("Invalid Input. Please enter a number")

    print("Select Operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Power")
    print("7. Square Root")
    print("8. Modulus")

    #   Initialize variables outside the loop
    num1 = 0
    num2 = 0

    # Take input from user
    while True:
        choice = input("Enter number correlating to choice: ")

        #   Check if choice is one of the listed options
        if choice in map(str, range(1, 8)):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        elif choice == '7':
            print(square_root(num1))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            num_str = input("Enter numbers in fraction format, i.e., First Number / Second Number: ")
            num1, num2 = map(float, num_str.split('/'))
            result = percentage(num1, num2)
            print(f"(num1) % (num2)= (result)%")
        elif choice == '6':
            print(num1, "^", num2, "=", power(num1, num2))
        elif choice == '7':
            print(math.sqrt(num1))
        elif choice == '8':
            print(num1, "/", num2, "=", modulus(num1, num2))

        #   Check if user wants another calculation
        #   Break the while loop if answer is no

        next_calculation = input("Do another calculation? (Yes/No): ")
        if next_calculation.lower() == "no":
            break
        if next_calculation.lower() == "yes":
            continue
        else:
            print("invalid input")

    print("Calculations Completed")
