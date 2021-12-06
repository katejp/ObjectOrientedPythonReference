def main():
	run_program = True
	while run_program == True:
		replacement_cost = getReplacementCost()
		insurance_amount = calculateInsurance(replacement_cost)
		printMessageInsuranceAmount(replacement_cost, insurance_amount)
		answer_yes_no = input("Would you like to get an insurance quote for another building? yes or no?   ")
		if answer_yes_no == "no":
			run_program = False

def getReplacementCost():
	replacement_cost = int(float(input("Enter the replacement cost of the building: $   ")))
	return replacement_cost

def calculateInsurance(replacement_cost):
	insurance_amount = int(float(replacement_cost * .80))
	return insurance_amount

def printMessageInsuranceAmount(replacement_cost, insurance_amount):
	print("The replacement cost of the building is $", format(replacement_cost, ',.2f'), ". It is recommended to purchase insurance for 80% of the building replacement cost. You should purchase $", format(insurance_amount, ',.2f'), "of insurance.")

main()