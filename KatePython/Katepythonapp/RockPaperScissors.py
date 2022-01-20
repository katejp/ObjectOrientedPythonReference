import random

def main():
	player_wins = 0
	ai_wins = 0
	user_number = DisplayMenu()
	if user_number == 1:
		user_answer_1, ai_answer_1 = PlayBestOf3()
	elif user_number == 2:
		DisplayStats()
	else:
		QuitGame()

def DisplayMenu():
	print("Kate's Famous Rock Paper Scissors")
	print("1: Play Best Of 3")
	print("2: Stats")
	print("3: Quit")
	number = int(input("Enter a number 1, 2, 3:   "))
	while number < 1 or number > 3 or number == 0:
		number = input("Oops! Please enter a number 1, 2, 3:   ")
	return number

def PlayBestOf3():
	rounds_played = 0
	player_round_wins = 0
	ai_round_wins = 0
	print("Game Instructions: Rock beats Scissors, Paper beats Rock, Scissors beats Paper.")
	print("Enter 1- Rock, 2- Paper, 3- Scissors")
	
	while player_round_wins != 2 or ai_round_wins != 2:

		# Play Round 
		PlayRound()

		# Display Result- modify rounds variables in playbestof3 function
	#check playbestof3 variables for who wins- modify main function variables
	


def PlayRound():
	
	answer_1 = int(input("Enter number:   "))
	
	if answer_1 == 1:
		print("Your answer is- Rock")
	elif answer_1 == 2:
		print("Your answer is- Paper")
	elif answer_1 == 3:
		print("Your answer is- Scissors")
	
	AI_answer_1 = random.randint(1, 3)
	
	if AI_answer_1 == 1:
		print("AI's answer is- Rock")
	elif AI_answer_1 == 2:
		print("AI's answer is- Paper")
	elif AI_answer_1 == 3:
		print("AI's answer is- Scissors")

	DisplayWinner(answer_1, AI_answer_1)
	return answer_1, AI_answer_1


def DisplayWinner(answer_1, AI_answer_1):
	if answer_1 == 1 and AI_answer_1 == 1:
		print("Rock and Rock is a tie.")
	elif answer_1 == 1 and AI_answer_1 == 2:
		print("Paper beats Rock. AI wins!")
	elif answer_1 == 1 and AI_answer_1 == 3:
		print("Rock beats Scissors. You win!")
	elif answer_1 == 2 and AI_answer_1 == 1:
		print("Paper beats Rock. You win!")
	elif answer_1 == 2 and AI_answer_1 == 2:
		print("Paper and Paper is a tie.")
	elif answer_1 == 2 and AI_answer_1 == 3:
		print("Scissors beats Paper. AI wins!")
	elif answer_1 == 3 and AI_answer_1 == 1:
		print("Rock beats Scissors. AI wins!")
	elif answer_1 == 3 and AI_answer_1 == 2:
		print("Scissors beats Paper. You win!")
	elif answer_1 == 3 and AI_answer_1 == 3:
		print("Scissors and Scissors is a tie.")
	
main()
	
