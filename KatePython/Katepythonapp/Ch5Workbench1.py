def main():
	run_program = True
	while run_program == True:
		user_number = int(input("Please enter a number:   "))
		if user_number < 0 or user_number > 100:
			print("Sorry! Let's try again. Please enter a number between 1 and 100:   ")
		product = user_number * 10
		print(product)
		userYesNo = input("Would you like to enter another number? Yes or No?   ")
		if userYesNo == "No":
			run_program = False
	

main()

# ?? A few problems with this code
# If 101 is entered "Sorry!" statement is written and user is prompted to enter a 
# new number, but the computer still tries to calculate the input and gives the product
# as 1010


