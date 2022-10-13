row_length = int(input("Length of the row: "))
end_post = int(input("End-post assembly length: "))
space_between_vines = int(input("Space between vines: "))

grapevines_per_row = (row_length - (2 * end_post)) / space_between_vines

print(f"You can fit {grapevines_per_row} grapevines in a row.")
