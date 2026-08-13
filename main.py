number = 63
attempts = 0

print("===== Number Guessing Game =====")
print("I have chosen a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct!")
        print(f"You guessed the number in {attempts} attempts.")
        break