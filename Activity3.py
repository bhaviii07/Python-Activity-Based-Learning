# Food Waste Monitoring System

print("FOOD WASTE MONITORING SYSTEM")

prepared = float(input("Enter food prepared (kg): "))
consumed = float(input("Enter food consumed (kg): "))

if prepared <= 0:
    print("Invalid prepared quantity")

elif consumed < 0 or consumed > prepared:
    print("Invalid consumed quantity")

else:
    wasted = prepared - consumed
    percentage = (wasted / prepared) * 100

    print("\n--- Food Waste Report ---")
    print("Food prepared:", prepared, "kg")
    print("Food consumed:", consumed, "kg")
    print("Food wasted:", wasted, "kg")
    print("Waste percentage:", round(percentage, 2), "%")

    if percentage >= 10:
        print("Status: Food waste is high.")
    else:
        print("Status: Food waste is low.")
