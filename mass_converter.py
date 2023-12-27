def mass_converter():
    print("Welcome to the mass converter. Please choose an option:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Ounces")
    print("4. Ounces to Grams")
    print("5. Metric Tons to Kilograms")
    print("6. Kilograms to Metric Tons")

    while True:
        choice_mass = input("Enter number correlating to choice: ")

        if choice_mass == '1':
            # KG to Pounds conversion
            kilograms = float(input("Enter mass in Kilograms: "))
            pounds = kilograms * 2.20462
            print(f"{kilograms} Kilograms is equal to {pounds:.2f} Pounds.")
        elif choice_mass == '2':
            # KG to Pounds conversion
            pounds = float(input("Enter mass in Pounds: "))
            kilograms = pounds * 0.453592
            print(f"{pounds} Pounds is equal to {kilograms:.2f} Kilograms.")
        elif choice_mass == '3':
            grams = float(input("Enter mass in Grams: "))
            ounces = grams * 0.03527396
            print(f"{grams} Grams is equal to {ounces:.2f} Ounces.")
        elif choice_mass == '4':
            ounces = float(input("Enter mass in Ounces: "))
            grams = ounces * 28.3495
            print(f"{ounces} Ounces is equal to {grams:.2f} Grams.")
        elif choice_mass == '5':
            metric_tons = float(input("Enter mass in Metric Tons: "))
            kilograms = metric_tons * 1000
            print(f"{metric_tons} Metric Tons is equal to {kilograms:.2f} Kilograms.")
        elif choice_mass == '6':
            kilograms = float(input("Enter mass in Kilograms: "))
            metric_tons = kilograms * 0.001
            print(f"{kilograms} Kilograms is equal to {metric_tons:.6f} Metric Tons.")
        else:
            print("Invalid choice. Please enter a number between 1-6.")

