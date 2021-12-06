
def main():
	billTotal = float(input("What is your bill total? $  "))
	reservationAnswer = input("Did you make a reservation with us tonight?   ")
	if reservationAnswer == "yes":
		print("As a thankyou for making a reservation with us tonight, 10% will be taken off your bill.")
		discount = .10
		GetDiscountedBillTotal(billTotal, discount)
	numberOfGuests = int(input("How many guests are in your party?  "))

	if numberOfGuests >= 6:
		print("It is custumary practice that if there are 6 or more guests in your party, then a Gratuity Charge of 20% is automatically applied")
		tipPercent = 20.0
		additionalTipYesNo = input("Would you like to leave an additional tip percentage?   ")
		if additionalTipYesNo == "yes":
			additionalTip = float(input("How much?   %"))
			tipPercent += additionalTip
	else:
		print("\n How much would you like to tip? \n")
	# Displays tip guide for user experience
		print("Tip Guide:")
		print("15% Minimum Courtesy Tip, Good Service")
		print("20% Customary Tip, Great Service, Recommended")
		print ("25% Beyond Excellent Service \n")
	# User inputs percentage they would like to tip
		tipPercent = float(input("  %"))

	tipPercent = TipPercentToDecimal(tipPercent)
	tipAmount = CalculateTipAmount(billTotal, tipPercent)
	BillGrandTotal(billTotal, tipAmount, tipPercent)
	
	
def GetDiscountedBillTotal(billTotal, discount):
	discountBillTotal = billTotal - (billTotal * discount)

def TipPercentToDecimal(tipPercent):
	tipPercentDecimal = tipPercent / 100
	return tipPercentDecimal

def CalculateTipAmount(billTotal, tipPercent):
	tipAmount = billTotal * tipPercent
	return tipAmount

def BillGrandTotal(billTotal, tipAmount, tipPercent):
	grandTotal = billTotal + tipAmount

	# Prints All Totals for user to see
	print("Totals: \n")
	print("Bill Total: $", round(billTotal, 2))
	print("Tip Percent: ", round(tipPercent, 2))
	print("Tip Amount: $", round(tipAmount, 2))
	print("Grand Total: $", round(grandTotal, 2))

main()
