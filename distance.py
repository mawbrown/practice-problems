print("How fast will you be driving?")
speed = input()

print("How long will you be driving?")
time = input()

distance = int(speed) * int(time)

print("If you continue driving at " + str(speed) + "mph,")
print("you will travel " + str(distance) + " miles.")
