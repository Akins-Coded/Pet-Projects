import random

def number_game():
    name = input("Hi,  What is your Name: ")

    print(f"🎲 Welcome to the Ultimate CODED Guessing Game, {name}!")
    ready = input(
        f"Are you ready to test your luck and wit, {name}? \n"
        f"Let's see if you can outsmart the computer! 🤖\n"
        f"Respond with yes or no: "
    ).strip().lower()

    if ready not in ['yes', 'y']:
        print(f"😞 I Knew It's You {name}, Don't you Like fun? ")
        print(f"😞 Oh come on {name}, don't be a party pooper! Maybe next time. Goodbye! 👋")
        return 
    
    print("\nI'm thinking of a number between 1 and 20.")
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
            print(f"\n🎉 Congratulations, {name}! I never had a doubt. 😉")
            print(f"You actually guessed it right: {secret_number} ✅")

            print(f"You still had {remaining_after} guess(es) left. Not bad at all!")
            print("You may now walk around like a champion. 🏆")
            print(f"Your new name should be *Winner {name}* 😜 Because you're The Undefeated! 🏆\n")
            break

        # Wrong guess: give sarcastic message + hint
        if guess < secret_number:
            hint = "The correct number is HIGHER than your guess."
        else:
            hint = "The correct number is LOWER than your guess."

        sarcastic_messages = [
            f"Wrong. But {name}, at least you're consistent. 😅",
            f"Nope. Guessing might not be your superpower, {name}, huh?",
            f"Incorrect, {name}. Maybe close your eyes and try again?",
            f"Ouch. That one hurt my circuits, {name}.",
            f"Still wrong, {name}. But I admire your confidence. 😂",
            f"Olodo lẹ́leyii sha! And your name {name} sounds like you know it all 😜"
        ]
        # Pick a sarcastic message based on attempt (just to vary a bit)
        message = sarcastic_messages[(attempt - 1) % len(sarcastic_messages)]

        print(message)
        print(f"💡 Hint: {hint}\n")

        # If this was the last guess, they lose
        if attempt == max_guesses:
            print(f"💀 Game Over, {name}!")
            print(f"The correct number was: {secret_number}")
            print("You used all 5 guesses and still missed it...")
            print(f"Your new name should be *Loser {name}* 😜 Better luck next time!\n")

if __name__ == "__main__":
    number_game()
