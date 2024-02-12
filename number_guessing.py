import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = 0
        self.min_range = 0
        self.max_range = 100
        self.attempts = 0
        self.playing = False

    def start_game(self):
        self.playing = True
        print("Welcome to the Number Guessing Game!")
        print("Challenge yourself and try to guess the randomly generated number.")
        self.select_range()

    def select_range(self):
        print("\nChoose the Range:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            self.max_range = 50
        elif choice == '3':
            self.max_range = 200
        else:
            self.max_range = 100

        self.generate_secret_number()

    def generate_secret_number(self):
        self.secret_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        print(f"\nI've picked a number between {self.min_range} and {self.max_range}. Let's begin!")

    def guess_number(self):
        while self.playing:
            try:
                guess = int(input("Enter your guess: "))
                self.attempts += 1
                if guess == self.secret_number:
                    print(f"Congratulations! You've guessed the number {self.secret_number} correctly in {self.attempts} attempts!")
                    self.playing = False
                    self.play_again()
                elif guess < self.secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Please enter a valid integer.")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            self.start_game()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()
    game.guess_number()
