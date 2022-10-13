sugar = 1.5
butter = 1
flour = 2.75
cookies = 48

new_cookies = int(input("How many cookies would you like to make? "))

new_sugar = sugar * new_cookies / cookies
new_butter = butter * new_cookies / cookies
new_flour = flour * new_cookies / cookies

print(f"Number of cookies wanted: {new_cookies}")
print(f"Total cups of sugar needed: {new_sugar}")
print(f"Total cups of butter needed: {new_butter}")
print(f"Total cups of flour needed: {new_flour}")
