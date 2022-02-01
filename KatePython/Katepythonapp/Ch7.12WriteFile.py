def main():
	number_file = open("number_count.txt", "w")
	for num in range(1, 11):
		number_file.write(str(num) + '\n')

	number_file.close()
	print("The numbers 1-10 have been written to the file number_count.txt")

main()