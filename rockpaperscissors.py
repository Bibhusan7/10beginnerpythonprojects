#rock paper scissors game
import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices) #computer choices random option from choices list

computer_score = 0 #storing computers score
player_score = 0 #storing players score

while True: #running while loop so game doesn't end until user wants to
    player = input("Rock, Paper or  Scissors?").capitalize()#capitalizing the input, so that user can input in small or lower case
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{computer_score}")
        print(f"Player:{player_score}")
        break