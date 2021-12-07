def main():
	run_program = True
	while run_program == True:
		monthly_loan_cost = getMonthlyCostOfLoanPayment()
		monthly_insurance_cost = getMonthlyCostOfInsurance()
		monthly_gas_cost = getMonthlyCostOfGas()
		monthly_oil_cost = getMonthlyCostOfOil()
		monthly_tire_cost = getMonthlyCostOfTires()
		monthly_maintenance_cost = getMonthlyCostOfMaintenance()
		monthly_total_expenses = displayTotalMonthlyExpenses(monthly_loan_cost, monthly_insurance_cost, monthly_gas_cost, monthly_oil_cost, monthly_tire_cost, monthly_maintenance_cost)
		displayTotalAnnualExpenses(monthly_total_expenses)
		answer_yes_no = input("Would you like to calculate the monthly and annual cost of another vehicle? yes or no?   ")
		if answer_yes_no == "no":
			run_program = False

def getMonthlyCostOfLoanPayment():
	monthly_loan_cost = float(input("Enter the loan payment monthly cost: $   "))
	return monthly_loan_cost

def getMonthlyCostOfInsurance():
	monthly_insurance_cost = float(input("Enter the monthly cost of insurance: $   "))
	return monthly_insurance_cost

def getMonthlyCostOfGas():
	monthly_gas_cost = float(input("Enter the monthly cost of gas: $   "))
	return monthly_gas_cost

def getMonthlyCostOfOil():
	monthly_oil_cost = float(input("Enter the monthly cost of oil: $   "))
	return monthly_oil_cost

def getMonthlyCostOfTires():
	monthly_tire_cost = float(input("Enter the monthly cost of tires: $   "))
	return monthly_tire_cost

def getMonthlyCostOfMaintenance():
	monthly_maintenance_cost = float(input("Enter the monthly cost of maintenance: $   "))
	return monthly_maintenance_cost

def displayTotalMonthlyExpenses(monthly_loan_cost, monthly_insurance_cost, monthly_gas_cost, monthly_oil_cost, monthly_tire_cost, monthly_maintenance_cost):
	monthly_total_expenses = monthly_loan_cost + monthly_insurance_cost + monthly_gas_cost + monthly_oil_cost + monthly_tire_cost + monthly_maintenance_cost
	print("Total Monthly Expenses: $", format(monthly_total_expenses, ',.2f'))
	return monthly_total_expenses

def displayTotalAnnualExpenses(monthly_total_expenses):
	annual_total_expenses = monthly_total_expenses * 12
	print("Total Annual Expenses: $", format(annual_total_expenses, ',.2f'))

main()