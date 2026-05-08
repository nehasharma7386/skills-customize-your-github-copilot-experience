#!/usr/bin/env python3
"""
Hangman Game - Python Implementation
A classic word-guessing game with visual feedback
"""

import random
import os
import sys


class HangmanGame:
    """Main Hangman Game class"""
    
    # Hangman ASCII art stages
    HANGMAN_STAGES = [
        # Stage 0 - Empty
        """
           +---+
           |   |
               |
               |
               |
               |
         =========
        """,
        # Stage 1 - Head
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========
        """,
        # Stage 2 - Body
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========
        """,
        # Stage 3 - Left arm
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========
        """,
        # Stage 4 - Both arms
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
         =========
        """,
        # Stage 5 - Left leg
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========
        """,
        # Stage 6 - Both legs (Game Over)
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         =========
        """
    ]
    
    # Word lists by category
    WORD_CATEGORIES = {
        'testing': [
            'SELENIUM', 'CUCUMBER', 'AUTOMATION', 'FRAMEWORK', 'JENKINS',
            'JUNIT', 'TESTCASE', 'VALIDATION', 'ASSERTION', 'REGRESSION'
        ],
        'payment': [
            'TRANSACTION', 'PAYMENT', 'SETTLEMENT', 'ROUTING', 'CLEARING',
            'RECONCILE', 'ACCOUNT', 'BALANCE', 'TRANSFER', 'DEPOSIT'
        ],
        'technology': [
            'PYTHON', 'JAVA', 'DATABASE', 'SERVER', 'NETWORK',
            'ALGORITHM', 'VARIABLE', 'FUNCTION', 'MODULE', 'PACKAGE'
        ],
        'animals': [
            'ELEPHANT', 'GIRAFFE', 'PENGUIN', 'DOLPHIN', 'KANGAROO',
            'BUTTERFLY', 'CHEETAH', 'OCTOPUS', 'FLAMINGO', 'RHINOCEROS'
        ],
        'countries': [
            'BRAZIL', 'CANADA', 'JAPAN', 'AUSTRALIA', 'FRANCE',
            'GERMANY', 'MEXICO', 'NORWAY', 'SWEDEN', 'PORTUGAL'
        ]
    }
    
    def __init__(self, max_attempts=6, category=None):
        """Initialize the game"""
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.guessed_letters = set()
        self.wrong_guesses = set()
        
        # Select category and word
        if category and category in self.WORD_CATEGORIES:
            self.category = category
            self.secret_word = random.choice(self.WORD_CATEGORIES[category])
        else:
            self.category = random.choice(list(self.WORD_CATEGORIES.keys()))
            self.secret_word = random.choice(self.WORD_CATEGORIES[self.category])
        
        self.game_won = False
        self.game_over = False
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_hangman(self):
        """Display the current hangman state"""
        wrong_count = self.max_attempts - self.attempts_left
        print(self.HANGMAN_STAGES[wrong_count])
    
    def get_display_word(self):
        """Get the word with guessed letters revealed"""
        return ' '.join(
            letter if letter in self.guessed_letters else '_'
            for letter in self.secret_word
        )
    
    def display_game_state(self):
        """Display the current game state"""
        self.clear_screen()
        print("=" * 50)
        print("           🎮 HANGMAN GAME 🎮")
        print("=" * 50)
        print(f"\nCategory: {self.category.upper()}")
        self.display_hangman()
        print(f"\nWord: {self.get_display_word()}")
        print(f"\nGuessed letters: {' '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print(f"Wrong guesses: {' '.join(sorted(self.wrong_guesses)) if self.wrong_guesses else 'None'}")
        print(f"Attempts remaining: {self.attempts_left}/{self.max_attempts}")
        print("=" * 50)
    
    def get_guess(self):
        """Get a valid letter guess from the player"""
        while True:
            guess = input("\nEnter a letter (or 'quit' to exit): ").upper().strip()
            
            if guess == 'QUIT':
                return None
            
            if len(guess) != 1:
                print("❌ Please enter a single letter!")
                continue
            
            if not guess.isalpha():
                print("❌ Please enter a valid letter!")
                continue
            
            if guess in self.guessed_letters:
                print("❌ You already guessed that letter!")
                continue
            
            return guess
    
    def process_guess(self, guess):
        """Process the player's guess"""
        self.guessed_letters.add(guess)
        
        if guess in self.secret_word:
            print(f"✅ Correct! The letter '{guess}' is in the word.")
            self.check_win()
        else:
            self.wrong_guesses.add(guess)
            self.attempts_left -= 1
            print(f"❌ Wrong! The letter '{guess}' is not in the word.")
            
            if self.attempts_left == 0:
                self.game_over = True
        
        input("\nPress Enter to continue...")
    
    def check_win(self):
        """Check if the player has won"""
        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.game_won = True
            self.game_over = True
    
    def display_final_result(self):
        """Display the final game result"""
        self.clear_screen()
        print("=" * 50)
        
        if self.game_won:
            print("🎉" * 10)
            print("\n     CONGRATULATIONS! YOU WON!")
            print(f"\n     The word was: {self.secret_word}")
            print(f"     Attempts used: {self.max_attempts - self.attempts_left}/{self.max_attempts}")
            print("\n" + "🎉" * 10)
        else:
            self.display_hangman()
            print("💀" * 10)
            print("\n        GAME OVER! YOU LOST!")
            print(f"\n     The word was: {self.secret_word}")
            print("\n" + "💀" * 10)
        
        print("=" * 50)
    
    def get_hint(self):
        """Provide a hint by revealing a random unguessed letter"""
        unguessed = [letter for letter in set(self.secret_word) 
                     if letter not in self.guessed_letters]
        
        if unguessed and self.attempts_left > 1:
            hint_letter = random.choice(unguessed)
            self.guessed_letters.add(hint_letter)
            self.attempts_left -= 1
            print(f"💡 Hint: The letter '{hint_letter}' is in the word!")
            print(f"⚠️  You lost one attempt for using a hint.")
            input("\nPress Enter to continue...")
            return True
        return False
    
    def play(self):
        """Main game loop"""
        print("\n" + "=" * 50)
        print("           Welcome to Hangman!")
        print("=" * 50)
        print("\nTry to guess the word letter by letter.")
        print(f"You have {self.max_attempts} attempts.")
        print("Type 'hint' for a hint (costs 1 attempt)")
        print("Type 'quit' to exit the game")
        input("\nPress Enter to start...")
        
        while not self.game_over:
            self.display_game_state()
            
            guess = self.get_guess()
            
            if guess is None:  # Player wants to quit
                print("\nThanks for playing!")
                return False
            
            if guess == 'HINT':
                if not self.get_hint():
                    print("❌ No hints available!")
                    input("\nPress Enter to continue...")
                continue
            
            self.process_guess(guess)
        
        self.display_final_result()
        return self.game_won


def display_menu():
    """Display the category selection menu"""
    print("\n" + "=" * 50)
    print("           SELECT A CATEGORY")
    print("=" * 50)
    categories = list(HangmanGame.WORD_CATEGORIES.keys())
    
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")
    print(f"{len(categories) + 1}. Random")
    print("0. Exit")
    print("=" * 50)
    
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                return None
            elif 1 <= choice <= len(categories):
                return categories[choice - 1]
            elif choice == len(categories) + 1:
                return None  # Random category
            else:
                print("❌ Invalid choice! Please try again.")
        except ValueError:
            print("❌ Please enter a number!")


def main():
    """Main function to run the game"""
    print("\n" + "🎮" * 25)
    print("         PYTHON HANGMAN GAME")
    print("🎮" * 25)
    
    wins = 0
    losses = 0
    
    while True:
        category = display_menu()
        
        if category is None and input("\nDo you want to exit? (yes/no): ").lower().startswith('y'):
            break
        
        game = HangmanGame(category=category)
        won = game.play()
        
        if won:
            wins += 1
        else:
            losses += 1
        
        print(f"\nScore - Wins: {wins} | Losses: {losses}")
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if not play_again.startswith('y'):
            break
    
    print("\n" + "=" * 50)
    print(f"Final Score - Wins: {wins} | Losses: {losses}")
    print("Thanks for playing! Goodbye! 👋")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye! 👋\n")
        sys.exit(0)
