def main ():
    print("Select Which Measurement You Want to Convert: \n")
    print("1. Temperature (Celsius & Farenheit) \n")
    print("2. Distance (km and m) \n")
    print("3. Weight (kg and g) \n")

    choice = str(input("\n Your Choice: "))

    if choice == "1" or choice == "Temperature":
            n = float(input(" \n Enter the value you want to convert: "))
            org_unit = input("\n Enter the original unit of the Number/value: ")
            con_unit = input("\n Enter the unit in which you want to convert the value: ")

            if org_unit == "F" or org_unit == "f" or org_unit == "Farenheit" or org_unit == "farenheit":
                final = (n-32)*(5/9)
                print("The Converted Temperature of ", n , org_unit , "is: ", final, con_unit, "\n")
            elif org_unit == "C" or org_unit == "c" or org_unit == "Celsius" or org_unit == "celsius" :
                final = n *(9/5)+32
                print("\n The Converted Temperature of ", n , org_unit , "is: ", final, con_unit, "\n")
            else:
                print("\n You Have chosen wrong Units. \n ")

    elif choice  == "2" or choice == "Distance":
            n = float(input(" \n Enter the value you want to convert: "))
            org_unit = input("\n Enter the original unit of the Number/value: ")
            con_unit = input("\n Enter the unit in which you want to convert the value: ")

            if org_unit == "km" or org_unit == "Km" or org_unit == "Kilometers" or org_unit == "kilometers" or org_unit=="KM" or org_unit == "kilometer" or org_unit == "Kilometer":
                final = n*1000
                print("\n The Converted Distance  of ", n , org_unit , "is: ", final, con_unit, "\n")
            elif org_unit == "m" or org_unit == "M" or org_unit == "Meter" or org_unit == "meter" or org_unit =="meters" or org_unit =="Meters":
                final = n/1000
                print("\n The Converted Distance of ", n , org_unit , "is: ", final, con_unit, "\n")
            else:
                print("\n You Have chosen wrong Units. \n ")

    elif choice  == "3" or choice == "Weight":
            n = float(input(" \n Enter the value you want to convert: "))
            org_unit = input("\n Enter the original unit of the Number/value: ")
            con_unit = input("\n Enter the unit in which you want to convert the value: ")

            if org_unit == "kg" or org_unit == "Kg" or org_unit == "Kilogram" or org_unit == "kilogram" or org_unit=="KG" or org_unit =="Kilograms" or org_unit =="kilograms":
                final = n*1000
                print("The Converted Weight of ", n , org_unit , "is: ", final, con_unit, "\n")
            elif org_unit == "g" or org_unit == "G" or org_unit == "Grams" or org_unit == "grams" or org_unit =="Gram" or org_unit =="gram":
                final = n/1000
                print("The Converted Weight of ", n , org_unit , "is: ", final, con_unit, "\n")
            else:
                print("\n You Have chosen wrong Units. \n ")

    else: 
       print("\n You have chosen the option outside of the menu.")
       print("\n Please select from the given menu for now \n ")

main ()
