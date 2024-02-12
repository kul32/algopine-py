import random

def roll_dice():
    return random.randint(1, 6)

def snake_ladder(position):
    snakes_and_ladders = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    if position in snakes_and_ladders:
        new_position = snakes_and_ladders[position]
        if new_position < position:
            print(f"Oops! Snake at {position}, go back to {new_position}")
        else:
            print(f"Yay! Ladder at {position}, climb up to {new_position}")
        return new_position
    return position

def play_game():
    player1_position = 1
    player2_position = 1

    while True:
        input("Player 1, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"Player 1 rolled a {dice_value}")
        player1_position += dice_value
        player1_position = snake_ladder(player1_position)
        print(f"Player 1 is at position {player1_position}")

        if player1_position >= 100:
            print("Player 1 wins!")
            break

        input("Player 2, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"Player 2 rolled a {dice_value}")
        player2_position += dice_value
        player2_position = snake_ladder(player2_position)
        print(f"Player 2 is at position {player2_position}")

        if player2_position >= 100:
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    play_game()
