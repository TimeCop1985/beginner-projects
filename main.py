import calculator
import mass_converter
import temp_converter


def application_menu():
    print("Welcome. Choose an option.")
    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. Mass Converter")
    print("4. Exit")


while True:
    application_menu()
    choice = input("Choose Application ")

    if choice == '1':
        calculator.calculator()
    elif choice == '2':
        temp_converter.temperature_converter()
    elif choice == '3':
        mass_converter.mass_converter()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid Choice. Please enter a number between 1-4.")
