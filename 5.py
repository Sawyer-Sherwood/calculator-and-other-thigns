attack_power = int(input("What is your attack power? "))
defense = int(input("What is the monster's defense? "))
health = int(input("What is the monster's health? "))

damage = attack_power - defense

if damage > 50:
	result = "CRITICAL HIT!"
elif damage > 20:
	result = "Solid hit!"
elif damage > 0:
	result = "awful hit."
else:
	result = "The monster dies laughing at your attack."

print(f"You dealt {damage} damage. {result}")

remaining_health = health - damage
if remaining_health > 0:
	print(f"The monster has {remaining_health} health left.")
else:
	print("The monster has been defeated.")
