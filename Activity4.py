#Multi-Product Price Fluctuation Analysis

print("MULTI-PRODUCT PRICE FLUCTUATION ANALYSIS")

n = int(input("Enter the number of products: "))

if n <= 0:
    print("Invalid number of products")

else:
    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        previous = float(input("Enter previous price: "))
        current = float(input("Enter current price: "))

        if previous <= 0 or current < 0:
            print("Invalid price")
            continue

        difference = current - previous
        percentage = (difference / previous) * 100

        print("\nProduct name:", name)
        print("Previous price: Rs.", previous)
        print("Current price: Rs.", current)
        print("Price difference: Rs.", round(difference, 2))
        print("Percentage change:", round(percentage, 2), "%")

        if difference > 0:
            print("Status: Price increased")
        elif difference < 0:
            print("Status: Price decreased")
        else:
            print("Status: Price unchanged")

print("\nAnalysis completed.")
