shares = 2000
cost_per_share = 40.00
total_cost = cost_per_share * shares
commission = 0.03 * total_cost
cost_and_commission = commission + total_cost

shares_sold = 2000
sold_per_share = 42.75
total_sold = shares_sold * sold_per_share
sold_commission = total_sold * 0.03
sold_and_commission = sold_commission + total_sold

profit = cost_and_commission - sold_and_commission

print(f"Joe paid ${total_cost} for the stock he bought.")
print(f"Joe had to pay ${commission} commission when buying the stock.")
print(f"Joe made ${total_sold} when selling the stock.")
print(f"Joe paid ${sold_commission} commission when selling the stock.")

print(f"Joe made a total of ${profit} profit.")
