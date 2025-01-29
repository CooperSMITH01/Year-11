import random

def play_game():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        try:
            guess = int(input("Guess a number: "))
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")
    print("YOU WIN!")

if __name__ == "__main__":
    play_game()
# Output:
# Guess a number: 50
# Too high!
# Guess a number: 25
# Too low!
# Guess a number: 37
# Too low!
# Guess a number: 43
# Too high!
# Guess a number: 40
# Too high!
# Guess a number: 38
# YOU WIN!
#
# Process finished with exit code 0