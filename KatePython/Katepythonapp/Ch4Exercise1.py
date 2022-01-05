def main():
	run_program = True
	while run_program == True:
		user_number = getNumberFromUser()
		displayNumberAsRomanNumeral(user_number)
		answer_yes_no = input("Would you like to enter another number?   ")
		if answer_yes_no == "no":
			run_program == False
		
		
def getNumberFromUser():
	number = 0
	while number < 1 or number > 10 or number == 0:
		number = int(input("Enter a number from 1-10:   "))
		if number < 1 or number > 10:
			print("Oh no! That is not a valid number. Enter a number between 1 and 10.")
	return number

def displayNumberAsRomanNumeral(number):
	if number == 1:
		print("I")
	elif number == 2:
		print("II")
	elif number == 3:
		print("III")
	elif number == 4:
		print("IV")
	elif number == 5:
		print("V")
	elif number == 6:
		print("VI")
	elif number == 7:
		print("VII")
	elif number == 8:
		print("VIII")
	elif number == 9:
		print("IX")
	elif number == 10:
		print("X")

main()


