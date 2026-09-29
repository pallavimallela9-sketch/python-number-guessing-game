import random

print("==========================================")
print("          NUMBER GUESSING GAME")
print("==========================================")

print("\nChoose a difficulty level:")
print("1. Easy   - 1 to 50")
print("2. Medium - 1 to 100")
print("3. Hard   - 1 to 500")

choice = input("Enter your choice: ")

if choice == "1":
    maximum = 50
    attempts_limit = 10
elif choice == "2":
    maximum = 100
    attempts_limit = 7
elif choice == "3":
    maximum = 500
    attempts_limit = 10
else:
    print("Invalid choice. Starting Medium level.")
    maximum = 100
    attempts_limit = 7

secret_number = random.randint(1, maximum)
attempts = 0
won = False

print("\nI have selected a number between 1 and", maximum)
print("You have", attempts_limit, "attempts to guess it.")

while attempts < attempts_limit:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > maximum:
        print("Enter a number within the given range.")
        continue

    attempts += 1

    if guess == secret_number:
        won = True
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Number of attempts:", attempts)
        break

    elif guess < secret_number:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")

    remaining = attempts_limit - attempts
    print("Attempts remaining:", remaining)

if not won:
    print("\nGame Over!")
    print("The correct number was:", secret_number)

print("\n==========================================")
print("              GAME RESULT")
print("==========================================")

if won:
    if attempts <= 3:
        print("Performance: Excellent")
    elif attempts <= 5:
        print("Performance: Good")
    else:
        print("Performance: Keep Practicing")
else:
    print("Performance: Try Again")

print("==========================================")
