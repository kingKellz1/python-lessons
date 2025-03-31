#Challenge 4
import random
import time

while True:
	print("*******************************************")
	print("-------------------------------------------")
	print("Welcome to the number guessing game!")
	print("___________________________________________")
	print("*******************************************")
	print("Select difficulty level:")
	print("1. Easy (1-50)")
	print("2. Medium (1-100)")
	print("3. Hard (1-1000)")
	print("Easy has a small range, Medium offers a medium range and Hard has a wider range")

	difficulty = int(input("Enter your choice: "))

	if difficulty == 1:
		random_number = random.randint(1, 50)
		print("I'm thinking of a number between 1 and 50.")
	elif difficulty == 2:
		random_number = random.randint(1, 100)
		print("I'm thinking of a number between 1 and 100.")
	elif difficulty == 3:
		random_number = random.randint(1, 1000)
		print("I'm thinking of a number between 1 and 1000.")
	else:
		print("Invalid choice, Setting to medium (1-100).")
		random_number = random.randint(1, 100)
		print("I'm thinking of a number between 1 and 100.")

	guess_count = 0

	start_time = time.time()

	while True:
		try:
			user_guess = int(input("Enter your guess: "))
			guess_count += 1
			if user_guess < random_number:
				print("Too low!")
			elif user_guess > random_number:
				print("Too high!")
			else:
				end_time = time.time()
				time_taken = end_time - start_time
				print(f"Correct! You guessed it in {guess_count} guesses")
				print(f"It took you {time_taken:.2f} seconds to guess the correct number.")
				break
		except ValueError:
			print("Please enter a number between 1 and 3.")

	play_again = input("Do you want to play again? (yes/no): ").lower()
	if play_again != 'yes':
		print("Thanks for playing!")
		break

