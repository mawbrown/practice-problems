purchase = input("Please enter your purchase amount: $")
state_tax = int(purchase) * 0.05
county_tax = int(purchase) * 0.025
sales_tax = state_tax + county_tax
total_price = int(purchase) + sales_tax

print("Based on your purchase amount, your tax and total price is the following:")
print("State tax: $" + str(state_tax))
print("County tax: $" + str(county_tax))
print("Total sales tax: $" + str(sales_tax))
print("Total price: $" + str(total_price))
