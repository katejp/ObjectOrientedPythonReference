def main():
	distanceToMiles()

def distanceToMiles():
	kilometers = (int(input("How many kilometers did you run today?   ")))
	miles = kilometers * 0.6214
	print("You ran", format(kilometers, '.2f'), "kilometers today and ran", format(miles, '.2f'), "miles today! Good job!")

main()

#____________________________________________________

def main():
	purchase_amount = float(int(input("What is the total of your purchase? $    ")))
	state_tax = computeStateTax(purchase_amount)
	county_tax = computeCountyTax(purchase_amount)
	total_sales_tax = computeTotalSalesTax(state_tax, county_tax)
	grand_total = computeGrandTotal(purchase_amount, total_sales_tax)
	printTotals(purchase_amount, state_tax, county_tax, total_sales_tax, grand_total)

def computeStateTax(purchase_amount):
	state_tax = purchase_amount * 0.04
	return state_tax

def computeCountyTax(purchase_amount):
	county_tax = purchase_amount * 0.02
	return county_tax

def computeTotalSalesTax(state_tax, county_tax):
	total_sales_tax = state_tax + county_tax
	return total_sales_tax

def computeGrandTotal(purchase_amount, total_sales_tax):
	grand_total = purchase_amount + total_sales_tax
	return grand_total

def printTotals(purchase_amount, state_tax, county_tax, total_sales_tax, grand_total):
	print("Purchase Amount: $", format(purchase_amount, '.2f'))
	print("State Tax: $", format(state_tax, '.2f'))
	print("County Tax: $", format(county_tax, '.2f'))
	print("Total Sales Tax: $", format(total_sales_tax, '.2f'))
	print("Grand Total: $", format(grand_total, '.2f'))

main()