import random
computer_choice = random.randint(1,3)
choices = ['rock', 'paper', 'scissors']
players_choice = input('Pick rock, paper, or scissors')

if not (players_choice in choices):
    print("Please pick either 'rock', 'paper', or 'scissors'")