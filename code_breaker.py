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

def generate_code():
	secret_code_list = random.sample(range(0,9+1), 3)
	secret_code = list_to_string(secret_code_list)	
	return secret_code

def get_clue(user_guess, secret_code):
	if user_guess == secret_code:
		print("\nyou have broken my secret code!!")
		return True
		
	output = "The hint for your guess is: {}"
	for i in range(len(user_guess)):
		if user_guess[i] == secret_code[i]:
			print(output.format('Match\n'))
			return False

		elif user_guess[i] in secret_code:
			print(output.format('Close\n'))
			return False

	print(output.format('None\n'))
	return False

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
	secret_code = generate_code()
	code_guessed = False

	while not code_guessed:
	 	user_guess = input('What is your guess? ')
	 	if len(user_guess) != 3 or type(int(user_guess)) != type(10):
	 		print('invalid input')
	 	else:
	 		code_guessed = get_clue(user_guess, secret_code)


if __name__ == '__main__':
	main()
