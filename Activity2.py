# Bus Passenger Occupancy Simulation

print("BUS PASSENGER OCCUPANCY SIMULATION")

capacity = int(input("Enter bus capacity: "))
current = int(input("Enter current passengers: "))
getting_off = int(input("Enter passengers getting off: "))
boarding = int(input("Enter passengers boarding: "))

if (capacity <= 0 or current < 0 or current > capacity
        or getting_off < 0 or boarding < 0):
    print("Invalid input")

elif getting_off > current:
    print("Invalid number of passengers getting off")

else:
    remaining = current - getting_off
    available = capacity - remaining

    print("\nPassengers after getting off:", remaining)
    print("Available seats:", available)

    if boarding > available:
        print("Bus capacity exceeded!")
        print("Maximum passengers allowed to board:", available)
    else:
        final = remaining + boarding
        seats = capacity - final

        print("Passengers after boarding:", final)
        print("Seats remaining:", seats)
        print("Bus occupancy simulation completed.")
