#Energy Conservation Before-and-After Analysis

print("ENERGY CONSERVATION ANALYSIS")

before = float(input("Enter electricity consumption before conservation (kWh): "))
after = float(input("Enter electricity consumption after conservation (kWh): "))

if before <= 0 or after < 0:
    print("Please enter valid electricity consumption values.")
elif after > before:
    print("Electricity consumption has increased.")
    print("Extra energy used:", after - before, "kWh")
else:
    saved = before - after
    percentage = (saved / before) * 100

    print("\n--- Results ---")
    print("Consumption before:", before, "kWh")
    print("Consumption after:", after, "kWh")
    print("Energy saved:", saved, "kWh")
    print("Energy reduction:", round(percentage, 2), "%")

    if saved > 0:
        print("Result: Energy conservation was successful!")
    else:
        print("Result: No energy was saved.")