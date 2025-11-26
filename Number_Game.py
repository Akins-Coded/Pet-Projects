import random

def number_guessing_game():
    print("🎲 Welcome to the Ultimate Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    print("You only have 5 guesses. Don't mess it up. 😏\n")

    secret_number = random.randint(1, 20)
    max_guesses = 5

    for attempt in range(1, max_guesses + 1):
        # Show remaining guesses at the start of each round
        remaining = max_guesses - attempt + 1
        print(f"👉 Guess #{attempt} (you have {remaining} guess(es) left)")

        # Get a valid integer guess
        try:
            guess = int(input("Enter your guess (1–20): "))
        except ValueError:
            print("🙄 That’s not even a number. Try again with an actual integer.\n")
            # This still consumes one attempt since user messed up
            continue

        if guess < 1 or guess > 20:
            print("🚫 Stay within 1 to 20, genius. That still counts as a guess.\n")
            continue

        # Correct guess
        if guess == secret_number:
            remaining_after = max_guesses - attempt
            print("\n🎉 Congratulations!")
            print(f"You actually guessed it right: {secret_number} ✅")

            print(f"You still had {remaining_after} guess(es) left. Not bad at all!")
            print("You may now walk around like a champion. 🏆\n")
            break

        # Wrong guess: give sarcastic message + hint
        if guess < secret_number:
            hint = "The correct number is HIGHER than your guess."
        else:
            hint = "The correct number is LOWER than your guess."

        sarcastic_messages = [
            "Wrong. But hey, at least you're consistent. 😅",
            "Nope. Math might not be your superpower, huh?",
            "Incorrect. Maybe close your eyes and try again?",
            "Ouch. That one hurt my circuits.",
            "Still wrong. But I admire your confidence. 😂"
        ]
        # Pick a sarcastic message based on attempt (just to vary a bit)
        message = sarcastic_messages[(attempt - 1) % len(sarcastic_messages)]

        print(f"{message}")
        print(f"💡 Hint: {hint}\n")

        # If this was the last guess, they lose
        if attempt == max_guesses:
            print("💀 Game Over!")
            print(f"The correct number was: {secret_number}")
            print("You used all 5 guesses and still missed it...")
            print("LOSER. (At this *game* only, relax 😜)\n")

if __name__ == "__main__":
    number_guessing_game()
