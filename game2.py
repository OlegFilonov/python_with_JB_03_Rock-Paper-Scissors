import random

lose_combinations = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
game_options = ['rock', 'paper', 'scissors']

def user_make_choice():
    user_choice = str(input())
    check_input(user_choice)
    

def check_input(string):
    if string == '!exit':
        print('Bye!')
    elif string in game_options:
        start_game(string)
    else:
        print("Invalid input")
        user_make_choice()

def start_game(string):
    computer_choice = random.choice(game_options)

    if string == computer_choice:
        print(f'There is a draw ({computer_choice})')
    elif lose_combinations[string] == computer_choice:
        print(f'Sorry, but the computer chose {computer_choice}')
    else:
        print(f'Well done. The computer chose {computer_choice} and failed')
    
    user_make_choice()

user_make_choice()
