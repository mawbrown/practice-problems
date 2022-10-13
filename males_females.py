total_students = int(input("How many students are in your class? "))
total_males = int(input("How many males are in your class? "))
total_females = int(input("How many females are in your class? "))

male_percentage = total_males / total_students * 100
female_percentage = total_females / total_students * 100

print(f"There are {total_students} students in your class.")
print(f"{male_percentage}% are males.")
print(f"{female_percentage}% are females.")
