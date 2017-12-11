# code_breaker.py - simple 3 digit number guessing game
'''
1. Program generates random 3 digit number
2. User inputs guess
3. Either user wins or computer gives clue

Clues:
Close - correct number but in wrong position
Match - One or more correct numbers in the right position
Nope - None correct at all

'''
import random

def welcome():
	print(
'''
Welcome to code_breaker.py. Lets see if you can guess my 3 digit number!
Code has been generated, please guess a 3 digit number.
'''
	)

def get_clue(user_guess, secret_code):
 	for i in range(len(user_guess)):
 		if user_guess[i] == secret_code[i]:
 			return 'Match'
 		elif user_guess[i] in secret_code:
 			return 'Close'

 	return 'None'


def list_to_string(a_list):
	'''Returns string form of list
	e.g. [1,2,3] -> "123"
	'''
	list_string = ""
	for item in a_list:
		list_string += str(item)

	return list_string

def main():
	welcome()
	# Generates 3 random numbers which are different from one another
	secret_code_list = random.sample(range(0,9+1), 3)
	secret_code = list_to_string(secret_code_list)
	# print(secret_code) use this to reveal secret code for debugging
	user_guess = ''
	while True:
	 	user_guess = input('What is your guess? ')
	 	if user_guess == secret_code:
	 		print("you have broken my secret code!!")
	 		break
	 	else:
	 		clue = get_clue(user_guess, secret_code)
	 		print(clue)

	 			

	

if __name__ == '__main__':
	main()