n = int(input("Give me a number between 1-100:   "))
if ((n % 2 == 0 and n >= 2 and n <= 5) or (n % 2 == 0 and n > 20)):
    print("Not Weird")
elif ((n % 2 != 0) or (n % 2 != 0 and n >= 6 and n <= 20)):
    print("Weird")
