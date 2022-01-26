def main():
	# d = 1/2*g*t^2
	# d is the distance in meters
	# g is 9.8
	# t is the amount in seconds that the object has been falling

	g = 9.8
	t = 0

	for seconds in range(1, 11):
		t += 1
		distance = falling_distance(g, t)
		print("The falling distance is", distance, "meters.")
	
def falling_distance(g, t):
	return 1/2 * g * (t ** 2)

main()
