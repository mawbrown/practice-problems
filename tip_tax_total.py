food_cost = input("How much was your food? $")
tip = 0.18 * int(food_cost)
sales_tax = 0.07 * int(food_cost)
total = int(food_cost) + tip + sales_tax

print("Your meal cost " + str(total) + ". This is with tip and tax included.")
