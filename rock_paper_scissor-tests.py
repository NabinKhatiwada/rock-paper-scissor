# Tests for rock-paper-scissors game (rock-paper-scissor.py)
import unittest
from unittest.mock import patch

from rock_paper_scissor import *

# Test 1: Test the computer's choice
class TestComputerChoice(unittest.TestCase):
    def test_computer_choice(self):
        self.assertIn(computerChoice(), ["rock", "paper", "scissor"])

# Test 2: Test the player's choice
class TestPlayerChoice(unittest.TestCase):
    def test_player_choice(self):
        self.assertEqual(playerChoice("s"), "scissor")

# Test 3: Test the winner
class TestWinner(unittest.TestCase):
    def test_winner(self):
        self.assertEqual(winner("rock", "paper"), "Player wins!")

class TestPlayAgain(unittest.TestCase):
    # Test 4: Test if game starts when player enters "y" on the playAgain function
    def test_play_again_yes_prompt(self):
        self.assertEqual(playAgain("y"), True)

    # Test 5: Test if game ends when player enters "n" on the playAgain function
    def test_play_again_no_prompt(self):
        self.assertEqual(playAgain("n"), False)

class TestQuitGame(unittest.TestCase):
    # Test 6: Test if game stops when player enters "y" on the quitGame function
    def test_quit_game_yes_prompt(self):
        self.assertEqual(quitGame("y"), True)

    # Test 7: Test if game continues when player enters "n" on the quitGame function
    def test_quit_game_no_prompt(self):
        self.assertEqual(quitGame("n"), False)

class TestGame(unittest.TestCase):
    # Test 8: Play the game for 5 rounds and don't play again
    @patch("builtins.input", side_effect=["s", "n", "r", "n", "p",  "n", "r", "n", "s", "y"])
    def test_game_no_again(self, input):
        self.assertEqual(game(), None)

    # Test 9: Play the game for 5 rounds and play again
    @patch("builtins.input", side_effect=["s", "n", "r", "n", "p",  "n", "r", "n", "s", "y", "y", "s", "n", "r", "n", "p",  "n", "r", "n", "s", "y"])
    def test_game_again(self, input):
        self.assertEqual(game(), None)

if __name__ == '__main__':
    unittest.main()