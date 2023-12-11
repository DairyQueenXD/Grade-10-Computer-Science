print("-------------------- Chow's R Us -------------------------")
new_customer = ""
num_customer = 1
total_revenue = 0
while new_customer != "n":
    print("\n>>>>> Customer " + str(num_customer) + " Receipt <<<<<")
    num_customer += 1
    new_purchases = ""
    total_cost = 0
    while new_purchases != "n":
        item_name = input("\nEnter Item Name: ")
        item_cost = float(input("Enter Item Cost: $"))
        total_cost = total_cost + item_cost
        total_cost_tax = total_cost*1.13
        new_purchases = input("Any other purchases (y/n)? ")
        while new_purchases != "n" and new_purchases != "y":
            print("You must input \"y\" or \"n\"!")
            new_purchases = input("Any other purchases (y/n)? ")
        if new_purchases == "n":
            print("\nTotal Cost before tax: $" + str(int(total_cost*100+0.5)/100))
            print("Total Cost after tax:  $" + str(int(total_cost_tax*100+0.5)/100))
    total_revenue = total_revenue + total_cost_tax
    total_revenue = int(total_revenue*100+0.5) / 100
    new_customer = input("Any other customers (y/n)? ")
    while new_customer != "y" and new_customer != "n":
        print("You must input \"y\" or \"n\"!")
        new_customer = input("Any other customers (y/n)? ")

print("\nTotal Revenue: $" + str(total_revenue))
print("\n-------------------- End of Receipt --------------------")
