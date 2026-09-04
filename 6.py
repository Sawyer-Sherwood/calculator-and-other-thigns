num_tacos = int(input("How many tacos would you like? "))
price_per_taco = float(input("How much does one taco cost? "))
age = int(input("How old are you? "))

original_total = num_tacos * price_per_taco

if num_tacos >= 10 and age < 18:
    discount = 0.25
elif num_tacos >= 10 or age < 18:
    discount = 0.10
else:
    discount = 0

final_total = original_total * (1 - discount)
title = "Taco Legend" if num_tacos >= 10 else "Taco Rookie"

print(f"Original total: ${original_total:.2f}")
print(f"Final total: ${final_total:.2f}")
print(f"You are officially a {title}!")