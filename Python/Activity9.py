#Warehouse Inventory Reconciliation

print("WAREHOUSE INVENTORY RECONCILIATION")

product = input("Enter product name: ")
recorded = int(input("Enter recorded stock quantity: "))
actual = int(input("Enter actual stock quantity: "))

if recorded < 0 or actual < 0:
    print("Invalid stock quantity. Enter values from 0 onwards.")

else:
    print("\n--- Inventory Report ---")
    print("Product name:", product)
    print("Recorded stock:", recorded)
    print("Actual stock:", actual)

    if actual == recorded:
        print("Status: Stock matches")
        print("Stock difference: 0")

    elif actual < recorded:
        shortage = recorded - actual
        print("Status: Stock shortage")
        print("Missing quantity:", shortage)

    else:
        extra = actual - recorded
        print("Status: Extra stock")
        print("Extra quantity:", extra)

    print("Inventory reconciliation completed.")
