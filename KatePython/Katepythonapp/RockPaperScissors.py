import random

def main():
	user_number = DisplayMenu()
	if user_number == 1:
		PlayBestOf3()
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
	wins_necessary = 2
	print("Game Instructions: Rock beats Scissors, Paper beats Rock, Scissors beats Paper.")
	
	while player_round_wins < 2 and ai_round_wins < 2:

		# Play Round 
		answer_1 = input("Enter R, P or S:   ")
		if answer_1 == "R":
			print("Your answer is- Rock")
		elif answer_1 == "P":
			print("Your answer is- Paper")
		elif answer_1 == "S":
			print("Your answer is- Scissors")
	
		AI_answer_1 = random.choice(["R", "P", "S"])
		if AI_answer_1 == "R":
			print("AI's answer is- Rock")
		elif AI_answer_1 == "P":
			print("AI's answer is- Paper")
		elif AI_answer_1 == "S":
			print("AI's answer is- Scissors")

		player_round_wins, ai_round_wins = DisplayWinner(answer_1, AI_answer_1, player_round_wins, ai_round_wins)
		print("Player Wins: ", player_round_wins)
		print("AI Wins: ", ai_round_wins)
		return answer_1, AI_answer_1, player_round_wins, ai_round_wins
	
def DisplayWinner(answer_1, AI_answer_1, player_round_wins, ai_round_wins):
	if answer_1 == "R" and AI_answer_1 == "R":
		print("Rock and Rock is a tie.")
	elif answer_1 == "R" and AI_answer_1 == "P":
		print("Paper beats Rock. AI wins!")
		ai_round_wins += 1
	elif answer_1 == "R" and AI_answer_1 == "S":
		print("Rock beats Scissors. You win!")
		player_round_wins += 1
	elif answer_1 == "P" and AI_answer_1 == "R":
		print("Paper beats Rock. You win!")
		player_round_wins += 1
	elif answer_1 == "P" and AI_answer_1 == "P":
		print("Paper and Paper is a tie.")
	elif answer_1 == "P" and AI_answer_1 == "S":
		print("Scissors beats Paper. AI wins!")
		ai_round_wins += 1
	elif answer_1 == "S" and AI_answer_1 == "R":
		print("Rock beats Scissors. AI wins!")
		ai_round_wins += 1
	elif answer_1 == "S" and AI_answer_1 == "P":
		print("Scissors beats Paper. You win!")
		player_round_wins += 1
	elif answer_1 == "S" and AI_answer_1 == "S":
		print("Scissors and Scissors is a tie.")

	return player_round_wins, ai_round_wins
		
	
main()
	
