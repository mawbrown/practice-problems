item1 = input("What is the total price of item one? $")
item2 = input("What is the total price of item two? $")
item3 = input("What is the total price of item three? $")
item4 = input("What is the total price of item four? $")
item5 = input("What is the total price of item five? $")
subtotal = int(item1) + int(item2) + int(item3) + int(item4) + int(item5)
sales_tax = subtotal * 0.07
total = subtotal + sales_tax

print("Your subtotal is $" + str(subtotal))
print("The tax amount is $" + str(sales_tax))
print("This brings your total to $" + str(total))
