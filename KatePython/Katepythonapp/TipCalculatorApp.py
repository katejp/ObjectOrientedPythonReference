
# User inputs bill total
billTotal = float(input("What is your bill total? $  "))

# User inputs if they made a reservation
reservationAnswer = input("Did you make a reservation with us tonight?   ")
if reservationAnswer == "yes":
	print("As a thankyou for making a reservation with us tonight, 10% will be taken off your bill.")
	billTotal = billTotal - (billTotal * .10) 

# User inputs how many guests in their party
numberOfGuests = int(input("How many guests are in your party?  "))

# Print this statement if user inputs a guest count of 6 persons or more
if numberOfGuests >= 6:
	print("It is custumary practice that if there are 6 or more guests in your party, then a Gratuity Charge of 20% is automatically applied")
	tipPercent = 20.0
	additionalTipYesNo = input("Would you like to leave an additional tip percentage?   ")
	if additionalTipYesNo == "yes":
		additionalTip = float(input("How much?   %"))
		tipPercent += additionalTip
	
# Prompt user for how much they would like to tip
else:
	print("\n How much would you like to tip? \n")
	# Displays tip guide for user experience
	print("Tip Guide:")
	print("15% Minimum Courtesy Tip, Good Service")
	print("20% Customary Tip, Great Service, Recommended")
	print ("25% Beyond Excellent Service \n")
	# User inputs percentage they would like to tip
	tipPercent = float(input("  %"))

# Reassigns users tip percentage input to a decimal number for later calculation
tipPercent = tipPercent / 100

# Calculates the tip amount by multiplying the tip percent by the bill total
tipAmount = billTotal * tipPercent 

# Calculates the grand total by adding the bill total and tip amount together
grandTotal = billTotal + tipAmount

# Prints All Totals for user to see
print("Totals: \n")
print("Bill Total: $", round(billTotal, 2))
print("Tip Percent: ", round(tipPercent, 2))
print("Tip Amount: $", round(tipAmount, 2))
print("Grand Total: $", round(grandTotal, 2))





