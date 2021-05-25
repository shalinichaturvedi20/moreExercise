from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    moves = ['rock', 'paper', 'scissors']
    random_move = randint(0, 2)
    computer_choice = moves[random_move]
    print(computer_choice)

    if player_choice == computer_choice:
        print ('Draw!')
    elif  player_choice and computer_choice == 'scissors':
        win()
    elif  player_choice and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and Computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice == 'paper' and computer_choice == 'rock':
        lose()
    player_choice1 = input('Do you want to play again? (y or n)')
    player_choice1.strip()
    if player_choice1 == 'n':
       break 