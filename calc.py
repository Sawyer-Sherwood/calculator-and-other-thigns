num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, /, *, or %): ")

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2
elif operator == "%":
    answer = num1 % num2
else:
    print("Invalid operator")
    answer = None

if answer is not None:
    print(f"{num1:.2f} {operator} {num2:.2f} = {answer:.2f}")