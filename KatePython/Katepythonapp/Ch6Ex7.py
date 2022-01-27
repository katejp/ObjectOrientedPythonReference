import random

def main():
	total_number = 0
	number_of_evens = 0
	number_of_odds = 0

	while total_number < 100:

		for number in range (1, 101):
			number = random.randint(1, 100)

			if is_even(number) == True:
				number_of_evens += 1
				total_number += 1

			else:
				number_of_odds += 1
				total_number += 1
	
		print("The number of random even numbers is", number_of_evens)
		print("The number of random odd numbers is", number_of_odds)

def is_even(number):
	if number % 2 == 0:
		return True

main()


