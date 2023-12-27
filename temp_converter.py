def temperature_converter():
    print("Welcome to the Temperature converter. Please choose an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Fahrenheit to Kelvin")
    print("4. Kelvin to Fahrenheit")
    print("5. Celsius to Kelvin")
    print("6. Kelvin to Celsius")

    while True:
        choice_temp = input("Enter number correlating to choice: ")

        # Check if choice is one of the listed options
        if choice_temp == '1':
            # Fahrenheit to Celsius conversion
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")

        elif choice_temp == '2':
            # Celsius to Fahrenheit conversion
            celsius = float(input("Enter temperature in Celsius"))
            fahrenheit = (celsius * 9 / 5) + 32

        elif choice_temp == '3':
            # Fahrenheit to Kelvin conversion
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
            print(f"{fahrenheit} Fahrenheit is equal to {kelvin:.2f} Kelvin.")

        elif choice_temp == '4':
            # Kelvin to Fahrenheit conversion
            kelvin = float(input("Enter temperature in Kelvin: "))
            fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
            print(f"{kelvin} Kelvin is equal to {fahrenheit:.2f} Fahrenheit.")

        elif choice_temp == '5':
            # Celsius to Kelvin conversion
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius + 273.15
            print(f"{celsius} Celsius is equal to {kelvin:.2f} Kelvin.")

        elif choice_temp == '6':
            # Kelvin to Celsius conversion
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin - 273.15
            print(f"{kelvin} Kelvin is equal to {celsius:.2f} Celsius.")

        else:
            print("Invalid choice. Please enter a number between 1-6.")

