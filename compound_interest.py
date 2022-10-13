P = float(input("Principal originally deposited into the account: $"))
r = float(input("Annual interest rate: "))
n = float(input("Number of times per year the interest is compounded: "))
t = float(input("Number of years the account will be left to earn interest: "))

r = r / 100

A = P * ((1 + (r / n))**(n * t))

print(A)
