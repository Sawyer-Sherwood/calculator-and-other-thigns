age = input ("how old are you: ") 
age = int(age) 
height = input ("how tall are you: ") 
height = int(height) 
if age >= 12 and height >= 150: 
    print ("You can ride the roller coaster!") 
elif age < 12 and height >= 150:
    print ("You are not old enough, but you are tall enough to ride the roller coaster.") 
else:
    print ("You are old enough but not tall enough to ride the roller coaster.") 

    print(f"required age: 12, your age: {age}") 
    print(f"required height: 150, your height: {height}") 

