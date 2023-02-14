#Classic Rock Paper Scissors game
#2 player Rock Paper Scissors game
print("===========================================")
print("Welcome to 🪨 Rock | 📄 Paper | ✂ Scissors!")
print("===========================================")
print()

#Get player 1 and 2 names and their selections
player1 = input("Player-1 What is your name? ")
player2 = input("Player-2 What is your name? ")
print()
print("=============================================")
print("Welcome to the game", player1, "and", player2)
print("Make your selections below:")
print("=============================================")
print()

#Get hidden players selections with input validation
from getpass import getpass as input
#player1
print(player1, "Please choose rock, paper, or scissors:")
player1_selection = input(": ")
if player1_selection != "rock" and player1_selection != "paper" and player1_selection != "scissors":
    print("Invalid input. Please choose rock, paper, or scissors.")
    print(player1, "Please choose rock, paper, or scissors:")
    player1_selection = input(": ")
print()

#player2
print(player2, "Please choose rock, paper, or scissors:")
player2_selection = input(": ")
if player2_selection != "rock" and player2_selection != "paper" and player2_selection != "scissors":
    print("Invalid input. Please choose rock, paper, or scissors.")
    player2_selection = input(": ")
print()

#Check Which player wins and print results

"""
Possible outcomes:
    Rock wins against scissors;
    paper wins against rock;
    scissors wins against paper
    If both players throw the same hand signal,
    it is considered a tie, and play resumes until there is a clear winner.
"""
if player1_selection == "rock" and player2_selection == "scissors":
    print("Rock crushes Scissors", player1, "Wins! 🥇🏆")
    print()
elif player1_selection == "paper" and player2_selection == "rock":
    print("Paper covers Rock", player1, "Wins! 🥇🏆")
    print()
elif player1_selection == "scissors" and player2_selection == "paper":
    print("Scissors cuts Paper", player1, "Wins! 🥇🏆")
    print()
elif player2_selection == "rock" and player1_selection == "scissors":
    print("Rock crushes Scissors", player2, "Wins! 🥇🏆")
    print()
elif player2_selection == "paper" and player1_selection == "rock":
    print("Paper covers Rock", player2, "Wins! 🥇🏆")
    print()
elif player2_selection == "scissors" and player1_selection == "paper":
    print("Scissors cuts Paper", player2, "Wins! 🥇🏆")
    print()
elif player1_selection == "rock" and player2_selection == "rock":
    print("It's clash of Rocks! What? Do wou want to cause an earthquake?")
    print()
elif player1_selection == "paper" and player2_selection == "paper":
    print("Paper covers Paper and Paper covers Paper, What a paper draw!")
    print()
else:
    print("It's a Tie of Scissors I've never seen that happen")
    print()