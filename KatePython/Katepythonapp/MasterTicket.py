# The Project
# Master Ticket

TICKET_PRICE = 10

tickets_remaining = 100

# Notify the user that the tickets are sold out if the tickets remaining is 0

if tickets_remaining == 0:
	print("I'm sorry we are sold out!")

# Run this code continuously until we run out of tickets

while tickets_remaining >= 1:

# Output how many tickets are remaining using the tickets_remaining variable 

	print("There are {} tickets remaining.".format(tickets_remaining)) 

# Gather the user's name and assign it to a new variable

	userName = input("What is your name?    ")

# Prompt the user by name and ask how many tickets they would like

	tickets_requested = input("How many tickets would you like, {}?  ".format(userName))
	
	#Try to coerce input to an integer. If the inoput given is greater than the tickets available, raise a ValueError.
	
	try:
		tickets_requested = int(tickets_requested)
		if tickets_requested > tickets_remaining:
			raise ValueError("Sorry! There are only {} tickets available for purchase.".format(tickets_remaining))

	# If the input is invalid, print this statement letting the user know
	
	except ValueError as err:
		print("Oh no, we ran into an issue. {}. Please try again.".format(err))

# Calculate the price (number of tickets multiplied by the price) and assign it to a variable
	else:
		amount_due = tickets_requested * TICKET_PRICE

# Output the price to the screen

		print("Your total today is $", amount_due)

# Prompt user if they want to proceed. Y/N?

		proceed_answer = input("Would you like to proceed? Yes/No?   ")

# If they want to proceed
	# Print out to the screen "Sold!" to confirm purchase
	# and then decrement the tickets remaining by the number of tickets purchased

	# sidenote: using the .lower function automatically converts whatver the input is to lowercase and then checks the conditions against that. 
	# therefore, it doesn't matter whether an uppercase or lowercase answer is entered. It will read it as lowercase.
		if proceed_answer.lower() == "yes":
			print("SOLD!")
			tickets_remaining -= tickets_requested
			print("There are {} tickets left remaining! Refer a friend for a special coupon!".format(tickets_remaining))
# TODO: Gather credit card information and process it 
# Otherwise... 
	# thank them by name

		else:
			print("Thank you anyways, {}. Have a great day!".format(userName))



