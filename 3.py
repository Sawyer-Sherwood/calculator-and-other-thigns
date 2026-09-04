amount = input("How many pizzas do you got?")
students = input("How many students are coming to the party?")

amount = int(amount)
students = int(students)

slices = amount * 8
per_student = slices / students

if per_student == 2:
    print("thats a good amount of pizza!")
elif per_student >= 3:
    print("way too much pizza!")
else:
    print("We're out of pizza, we need more!!")

print(f"num. of students - {students}")
print(f"Total Slices: {slices}")
print(f"Debug: {per_student}") 
