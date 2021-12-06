def main():
	timesTen()

def timesTen():
	number = int(input("Give a number:   "))
	result = number * 10
	print(result)

main()

#____________________________________

def main():
	x = 1
	y = 3.4
	print(x, y)
	change_us(x, y)
	print(x, y)

def change_us(a, b):
	a = 0
	b = 0
	print(a, b)

main()

#________________________________________

def my_function(a, b, c):
	d = (a + c) / b
	print(d)

my_function(a=2, b=4, c=6)