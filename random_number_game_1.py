import random


def get_hint(low, high):
    return (low + high) // 2


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