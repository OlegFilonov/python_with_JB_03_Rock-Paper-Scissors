import random

lose_combinations = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
default_options = ['rock', 'paper', 'scissors']


def get_user_name():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    rating = open('rating.txt', 'r')
    for item in rating:
        if user_name in item:
            user_score = [int(s) for s in item.split() if s.isdigit()][0]
        else:
            user_score = 0

        user_choose_game(user_score)
        # user_make_choice(user_score)


def user_choose_game(user_score, game_options='default'):
    game_option = str(input())
    print("Okay, let's start")
    # default option game
    if game_option == '':
        user_make_choice(user_score, game_options)
    # user option game
    else:
        user_options = game_option.split(',')
        game_options = 'user_game'
        user_make_choice(user_score, game_options, user_options)


def user_make_choice(user_score, game_options=None, user_options=None):
    user_choice = str(input())
    check_input(user_choice, user_score, game_options, user_options)


def check_input(string, user_score, game_options, user_options):
    if string == '!exit':
        print('Bye!')
        exit()
    elif string == '!rating':
        print(f'Your rating: {user_score}')
        user_make_choice(user_score, game_options, user_options)
    elif game_options == 'user_game':
        if string in user_options:
            start_game(string, user_score, game_options, user_options)        
        else:
            print("Invalid input")
            user_make_choice(user_score)            
    elif game_options == 'default':     
        if string in default_options:
            start_game(string, user_score, game_options, user_options)
        else:
            print("Invalid input")
            user_make_choice(user_score, game_options, user_options)


def start_game(string, user_score, game_options, user_options):
    if game_options == 'user_game':
        play_user_game(string, user_score, user_options)
    else:
        play_default_game(string, user_score, game_options)

    
def play_default_game(string, user_score, game_options):
    
    computer_choice = random.choice(default_options)
    
    if string == computer_choice:
        user_score += 50
        print(f'There is a draw ({computer_choice})')
    elif lose_combinations[string] == computer_choice:
        print(f'Sorry, but the computer chose {computer_choice}')
    else:
        user_score += 100
        print(f'Well done. The computer chose {computer_choice} and failed')
    
    user_make_choice(user_score, game_options)


def play_user_game(string, user_score, user_options):

    computer_choice = random.choice(user_options)
    user_item = user_options.index(string)
    win_lose_list = user_options[(user_item+1):] + user_options[:user_item]
    lose_list = win_lose_list[:int((len(win_lose_list)/2))]
    win_list = win_lose_list[int((len(win_lose_list)/2)):]

    if string == computer_choice:
        user_score += 50
        print(f'There is a draw ({computer_choice})')

    elif computer_choice in lose_list:
        print(f'Sorry, but the computer chose {computer_choice}')

    elif computer_choice in win_list:
        user_score += 100
        print(f'Well done. The computer chose {computer_choice} and failed')

    game_options = 'user_game'
    user_make_choice(user_score, game_options, user_options)

get_user_name()
