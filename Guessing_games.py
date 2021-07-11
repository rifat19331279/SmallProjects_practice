from random import randint
import sys

ans= randint(int(sys.argv[1]), int(sys.argv[2]))

def guessing(guess, ans):
	guess=int(guess)
	if (int(sys.argv[1])-1)< guess < (int(sys.argv[2])+1):

		if guess == ans:
			print('you WIN!')
			return True

		if guess != ans:
			print(f'you only have 3 chances! Used {i+1}!')

		if i==2 and guess != ans:
			print('you LOSE!')

	if guess>=(int(sys.argv[2])+1):
		print('Too big! Enter a number between 1 to 10')
		print(f'you only have 3 chances! Used {i+1}!')
		return False


if __name__=='__main__':
	while True:
		for i in range(3):
			try:
				guess=input(f'Guess a number from {sys.argv[1]} to {sys.argv[2]}: ')
				print(ans)
				if (guessing(guess, ans))==True:
					break
			except ValueError as err:
				print(f'Please do not enter anything other than numbers.')
				print(f'you only have 3 chances! Used {i+1}!')
				continue

			except TypeError as err2:
				continue
		break
					
		
