import random

def play_game():
    number = random.randint(1, 100)
    low, high = 1, 100
    guess = None
    while guess != number:
        guess = (low + high) // 2
        print(f"Guessing: {guess}")
        if guess < number:
            print("Too low!")
            low = guess + 1
        elif guess > number:
            print("Too high!")
            high = guess - 1
    print("YOU WIN!")

if __name__ == "__main__":
    play_game()