import random

class RockPaperScissor:
    options = ['rock', 'paper', 'scissors']
    
    turns = 5

    necessary_wins = turns

    player_wins = 0
    computer_wins = 0

    while True:

        while True:
            player = input(">>> rock, paper, scissors: ")
            if player in options:
                break

        computer = random.choice(options)

        if player == computer:
            print('It is a tie')
        elif player == 'rock' and computer == 'paper':
            print('Computer wins, paper covers rock')
            computer_wins += 1
        elif player == 'rock' and computer == 'scissors':
            print('You win, rock smashes scissors')
            player_wins += 1
        elif player == 'paper' and computer == 'rock':
            print('You win, paper covers rock')
            player_wins += 1
        elif player == 'paper' and computer == 'scissors':
            print('Computer wins, scissors cut paper')
            computer_wins += 1
        elif player == 'scissors' and computer == 'rock':
            print('Computer wins, rock smashes scissors')
            computer_wins += 1
        elif player == 'scissors' and computer == 'paper':
            print('You win, scissors cut paper')
            player_wins += 1

        if player_wins == necessary_wins or computer_wins == necessary_wins:
            break

    if player_wins > computer_wins:
        print(f'>>> You win! <<<')
    else:
        print(f'>>> Computer wins! <<<')

    print(f'>>> You scored: {player_wins} point(s) <<<')