import random


def get_hint(low, high):
    return (low + high) // 2


def play_game():
    number = random.randint(1, 100)
    low, high = 1, 100
    guess = None
    while guess != number:
        try:
            guess = int(input(f"Guess a number between {low} and {high} (Hint: {get_hint(low, high)}): "))
            if guess < number:
                print("Too low!")
                low = guess + 1
            elif guess > number:
                print("Too high!")
                high = guess - 1
        except ValueError:
            print("Please enter a valid number.")
    print("YOU WIN!")


if __name__ == "__main__":
    play_game()

#  this version was created during a GitHub chat session with a user who wanted to add a hint to the game.
#  it was also done with github chat to show that it works very well