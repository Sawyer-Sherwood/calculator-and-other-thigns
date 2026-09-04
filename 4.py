agent = input("What is your Agent Number: ")
level = int(input("What is your Security Level: "))

if agent == "007" or level >= 5:
	print("ACCESS GRANTED")
elif level == 0:
	print("SECURITY ALERT! Nice try.")
else:
	print("ACCESS DENIED, you are not authorized to access this system LOSER!") 
	
