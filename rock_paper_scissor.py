import random

# global point counters for the player and the computer
# global total rounds
player_point = 0
computer_point = 0
total_rounds = 0

# The computer randomly picks one of the options of scissor, paper and rock.
def computerChoice():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "scissor"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "rock"
    return computer_choice

# Player is then given the option to pick/type one of the options of scissor, paper and rock.
def playerChoice(player_choice):
    if player_choice == "s" or player_choice == "S":
        player_choice = "scissor"
    elif player_choice == "p" or player_choice == "P":
        player_choice = "paper"
    elif player_choice == "r" or player_choice == "R":
        player_choice = "rock"
    else:
        player_choice = "invalid"
    return player_choice

# One point is given to the winner.
def winner(computer_choice, player_choice):
    global player_point, computer_point
    return_text = ""
    if computer_choice == player_choice:
        return_text = "It's a tie!"
    elif computer_choice == "scissor":
        if player_choice == "paper":
            return_text = "Computer wins!"
            computer_point += 1
        else:
            return_text = "Player wins!"
            player_point += 1
    elif computer_choice == "paper":
        if player_choice == "rock":
            return_text = "Computer wins!"
            computer_point += 1
        else:
            return_text = "Player wins!"
            player_point += 1
    elif computer_choice == "rock":
        if player_choice == "scissor":
            return_text = "Computer wins!"
            computer_point += 1
        else:
            return_text = "Player wins!"
            player_point += 1
    return return_text

# The total number of rounds played in total will also be displayed.
def totalRounds():
    global total_rounds
    total_rounds += 1
    return "Total rounds played: ", total_rounds

# Once the winner is determined, the player is asked to quit or restart the game
def playAgain(play_again):
    if play_again == "y" or play_again == "Y":
        play_again = True
    elif play_again == "n" or play_again == "N":
        play_again = False
    else:
        play_again = "invalid"
    return play_again

# Player can also quit the game at any time.
def quitGame(quit_game):
    if quit_game == "y" or quit_game == "Y":
        quit_game = True
    elif quit_game == "n" or quit_game == "N":
        quit_game = False
    else:
        quit_game = "invalid"
    return quit_game

# Asks user to play again or not
def askPlayAgain():
    play_again = input("Do you want to play again? (y/n): ")
    play_again = playAgain(play_again)
    if play_again == True:
        # resets the point counter for the player and the computer and total rounds
        global player_point, computer_point, total_rounds
        player_point = 0
        computer_point = 0
        total_rounds = 0
        game()
    elif play_again == False:
        print("\nThank you for playing!")
    else:
        print("Invalid choice. Please try again.")
        askPlayAgain()

# The first to get five points wins the game.
def game():
    global player_point, computer_point
    while True:
        computer_choice = computerChoice()
        player_choice = input("Choose scissor (s), paper (p), or rock (r): ")
        player_choice = playerChoice(player_choice)
        if player_choice == "invalid":
            print("Invalid choice. Please try again.")
            continue
        else:
            print(totalRounds())
        print(winner(computer_choice, player_choice))
        print("Player: ", player_point)
        print("Computer: ", computer_point)
        if player_point >= 5:
            print("\nPlayer wins all round!\n")
            askPlayAgain()
            break
        elif computer_point >= 5:
            print("\nComputer wins all round!\n")
            askPlayAgain()
            break
        quit_game = input("Do you want to quit the game? (y/n): ")
        quit_game = quitGame(quit_game)
        if quit_game == True:
            print("\nThank you for playing!")
            break
        
# Run the game
if __name__ == "__main__":
    game()
