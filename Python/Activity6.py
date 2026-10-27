#Traffic Violation Penalty Calculator

print("TRAFFIC VIOLATION PENALTY CALCULATOR")

print("\n1. Overspeeding - Rs. 1000")
print("2. Riding without helmet - Rs. 500")
print("3. Jumping red signal - Rs. 1000")
print("4. Not wearing seat belt - Rs. 500")

choice = int(input("\nEnter your violation choice (1-4): "))

if choice == 1:
    violation = "Overspeeding"
    fine = 1000

elif choice == 2:
    violation = "Riding without helmet"
    fine = 500

elif choice == 3:
    violation = "Jumping red signal"
    fine = 1000

elif choice == 4:
    violation = "Not wearing seat belt"
    fine = 500

else:
    violation = ""
    fine = 0
    print("Invalid choice. Please select from 1 to 4.")

if choice in [1, 2, 3, 4]:
    print("\n--- Penalty Details ---")
    print("Violation:", violation)
    print("Penalty amount: Rs.", fine)
