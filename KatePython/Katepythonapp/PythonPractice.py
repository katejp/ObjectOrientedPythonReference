firstName = input("What is your name?   ")
print("hello,", firstName)
if firstName == "Kate":
	print(firstName, "is learning python")
elif firstName == "Peek":
	print(firstName, "is learning with fellow students in the community!")
else:
	# this is just in case we have a younger user who can't yet read
	age = int(input("How old are you?  "))
	if age <= 6:
		print("Wow, you're {}! If you're confident with your reading already...".format(age))
	print("You should totally learn Python, {}!".format(firstName))
print("Have a great day {}!".format(firstName))

praise = "You are doing great"
praise = praise.upper()
number_of_characters = len(praise)
result = praise + "!" * number_of_characters
print(result)

def multiplyTwoNumbers(num5, num6):
	num3 = num5 * num6
	print("The answer to your multiplied numbers is {}".format(num3))


multiplyTwoNumbers(5, 10)

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep things DRY.")

# Check Please

import math

def split_check(total, number_of_people):
	return math.ceil(total / number_of_people)

total_due = float(input("What is the total?   "))
number_of_people = int(input("How many people?  "))

amount_due = split_check(total_due, number_of_people)
print("Each person owes ${}".format(amount_due))
_______________________________________________________________________________

# Expecting Exceptions
import math

def split_check(total, number_of_people):
	return math.ceil(total / number_of_people)
try:
    total_due = float(input("What is the total?   "))
    number_of_people = int(input("How many people?  "))
except ValueError:
    print("Oh no! That's not a valid value. Try again...")
else:
    amount_due = split_check(total_due, number_of_people)
    print("Each person owes ${}".format(amount_due))

____________________________________________________________________________

# Raising Exceptions

import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)
try:
    total_due = float(input("What is the total? $   "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:    
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))

___________________________________________________________________________

# While Loops

import sys

MASTER_PASSWORD = "opensesame"
password = input("Please enter the super secret password:    ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again:    ")
    attempt_count += 1
print("Welcome to secret town")

# For Loops
    #see notes



