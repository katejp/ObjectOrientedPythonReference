def main():
	number1 = int(input("Give me a number:    "))
	number2 = int(input("Give me another number:    "))
	Result = multiplyTwoNumbers(number1, number2)
	print("The result of", number1, "and", number2, "is", Result)

def multiplyTwoNumbers(number1, number2):
	multipliedNumber = number1 * number2
	return multipliedNumber

main()

#____________________________________________________________________________________________________________________

def main():
	run_program = True
	while run_program == True:
		number1 = int(input("Give me a number:    "))
		number2 = int(input("Give me another number:    "))
		multiplyTwoNumbers(number1, number2)
		answerYesNo = input("Would you like to multiply another number? yes or no?    ")
		if answerYesNo == "no":
			run_program = False

def multiplyTwoNumbers(number1, number2):
	multipliedNumber = number1 * number2
	print("The result of", number1, "and", number2, "is", multipliedNumber)

main()

