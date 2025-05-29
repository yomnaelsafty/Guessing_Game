import random

def guessing_game():
    print("🎉 Welcome to the Guessing Game! 🎉")

    min_attempts = None

    while True:
        pc_number = random.randint(1, 10)
        attempts = 0
        print("\nI've picked a number between 1 and 10.")
        print("Can you guess what it is?")

        while True:
            try:
                player_guess = int(input("Your guess: "))
                if player_guess < 1 or player_guess > 10:
                    print("🚫 Please pick a number between 1 and 10.")
                    continue
            except ValueError:
                print("🚫 That's not a valid number. Try again!")
                continue

            attempts += 1

            if player_guess == pc_number:
                print(f"🎉 You got it right in {attempts} attempt(s)! You're amazing! 🥳")
                if min_attempts is None or attempts < min_attempts:
                    min_attempts = attempts
                    print("🌟 New record! That's your best try so far!")
                else:
                    print(f"🔁 Your best is still {min_attempts} attempt(s). Keep trying!")
                break
            elif player_guess < pc_number:
                print("🔼 Too low! Try a higher number.")
            else:
                print("🔽 Too high! Try a lower number.")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing! See you next time.")
            break

# Start the game
guessing_game()
