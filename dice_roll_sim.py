from random import randint

play_again = 'yes'

while play_again == 'yes':
	comp_no = randint(1, 6)
	user_no = randint(1, 6)
	print("Computer Number:", comp_no)
	print("User Number:", user_no)
	if comp_no > user_no:
		print("Computer wins!")
	elif user_no > comp_no:
		print("User wins!")
	else:
		print("No winner. It's a draw.")
		print("------------------------")
		continue

	play_again = input("Enter 'yes' to play again: ")
