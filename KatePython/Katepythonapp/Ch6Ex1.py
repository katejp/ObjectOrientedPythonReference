def main():
	number_feet = int(input("Enter the number of feet:   "))
	result = feet_to_inches(number_feet)
	print(number_feet, "feet is equal to", result, "inches.")

def feet_to_inches(number):
	return number * 12

main()