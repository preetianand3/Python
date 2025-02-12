from random import shuffle

def shuffle_list(mylist):
	shuffle(mylist)
	return mylist


def player_guess():
	guess = ''

	while guess not in ['0', '1', '2']:
		guess = input("Pick a number: 0, 1 or 2: ")

	return int(guess)

def check_guess(mylist, guess):
	if mylist[guess] == 'O':
		print("Correct guess")
	else:
		print("better luck next time")
		print(mylist)


mylist = [' ', 'O', ' ']

print("*****THREE CUP MONTE*****")
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list, guess)