def main():
	getBillTotal()
	getNumberOfGuests()

def getBillTotal():
	bill_total = int(float(input("What is your bill total? $   ")))
	print("Your bill total is", bill_total)

def getNumberOfGuests():
	number_of_guests = int(input("What is the number of guests in your party?   "))
	print("The number of guests in your party is", number_of_guests)

main()
