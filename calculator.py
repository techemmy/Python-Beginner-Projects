from math import *

while True:
	expr = input(":>")
	if not expr:
	   continue
	if expr == "q":
		break
	print(eval(expr))
