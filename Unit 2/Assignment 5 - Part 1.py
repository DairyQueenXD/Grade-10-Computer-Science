print("-------------------- Chow Mobile --------------------")

total_cost = 0
phone_calls = int(input("Number of long distance phone calls made: "))
for i in range(phone_calls):
    cost = 0
    minutes = int(input("\nNumber of minutes for call #" + str(i+1) + ": "))
    if minutes <= 3:
        cost = 1.24
    else:
        cost = 1.24 + 0.76*(minutes - 3)
        cost = int(cost*100+0.5)/100
    total_cost = total_cost + cost
    total_cost = int(total_cost*100+0.5)/100
    print("\nCost for call #" + str(i+1) + ": $" + str(cost))
    print(("Total cost of all calls: $") + str(total_cost))
print("-------------------- THANK YOU --------------------")





