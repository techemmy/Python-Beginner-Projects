year = int(input("Enter the year to find out > "))

if (year % 100 == 0) and (year % 400 != 0):
	print("Hmmm. Not a leap year.")
elif (year % 4 == 0):
	print("It's a leap year.")
else:
	print("not a step close.")
