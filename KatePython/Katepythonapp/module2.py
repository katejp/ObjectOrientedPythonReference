# The Project
# Master Ticket

TICKET_PRICE = 10
tickets_remaining = 100

if tickets_remaining == 0:
	print("I'm sorry we are sold out!")

while tickets_remaining >= 1: 
	print("There are {} tickets remaining.".format(tickets_remaining)) 
	userName = input("What is your name?    ")
	tickets_requested = input("How many tickets would you like, {}?  ".format(userName))
	if tickets_requested > tickets_remaining:
			raise ValueError("Sorry! There are only {} tickets available for purchase.".format(tickets_remaining))
		
	tickets_requested = int(tickets_requested)
		
	except ValueError as err:
		print("Oh no, we ran into an issue. Please try again.")
		print("({})".format(err))
	else:
		amount_due = tickets_requested * TICKET_PRICE
		print("Your total today is $", amount_due)
		proceed_answer = input("Would you like to proceed? Yes/No?   ")

		if proceed_answer.lower() == "yes":
			print("SOLD!")
			tickets_remaining -= tickets_requested
			print("There are {} tickets left remaining! Refer a friend for a special coupon!".format(tickets_remaining))

		else:
			print("Thank you anyways, {}. Have a great day!".format(userName))
