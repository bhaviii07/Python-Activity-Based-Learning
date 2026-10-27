#Multi-Product Shopping Budget Constraint

print("MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT")

budget = float(input("Enter your shopping budget (Rs.): "))
n = int(input("Enter the number of products: "))

if budget <= 0 or n <= 0:
    print("Invalid budget or number of products.")

else:
    total = 0
    valid = True

    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        price = float(input("Enter product price (Rs.): "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid product details.")
            valid = False
            break

        cost = price * quantity
        total += cost

        print("Product:", name)
        print("Product cost: Rs.", round(cost, 2))

    if valid:
        print("\n--- Shopping Summary ---")
        print("Available budget: Rs.", round(budget, 2))
        print("Total shopping cost: Rs.", round(total, 2))

        if total <= budget:
            remaining = budget - total
            print("Status: Shopping is within budget.")
            print("Remaining budget: Rs.", round(remaining, 2))
        else:
            extra = total - budget
            print("Status: Budget exceeded.")
            print("Extra amount required: Rs.", round(extra, 2))

    else:
        print("Shopping calculation stopped due to invalid details.")
