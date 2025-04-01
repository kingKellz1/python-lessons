import random

#Guessing game:
"""you guess a number and the program checks if it's correct
correct_number = 7
attempts = 0

while True:

	guess = int(input("Guess a number: "))
	attempts += 1
	if guess == correct_number:
		print(f"Correct! It took you {attempts} attempts.")
		break
	elif guess < correct_number:
		print("Too low! Try again.")
	else:
		print("Too high! Try again")
"""

#Odd or Even
"""
while True:
	user_num = input("Enter a number: ")
	if user_num.lower() == "stop":
		print("Exiting the program.")
		break
	else:
		try:
			num = int(user_num)
			if num % 2 == 0:
				print(f"{num} is even")
			else:
				print(f"{num} is odd")
		except ValueError:
			print("Invalid input! Please enter a valid number or 'stop' to exit.")
"""

#Future Age
"""
while True:
	try:
		user_name = input("Please enter your name: ")
		user_age = int(input("Please enter your age: "))
		if user_age < 0:
			print("Please enter a positive number")
			continue #Skips the rest and prompt again
		user_num = int(input("How many years in the future would you want to calculate? "))
		if user_num < 0:
			print("Please enter a positive number")
			continue #Skips the rest and prompt again
		future_age = user_age + user_num
		print(f"Your name is: {user_name}, your current age is: {user_age}")
		print(f"In {user_num} years, {user_name} will be {future_age} years old")
		break
	except ValueError:
		print("Invalid input, Please enter a valid number (non negative)")
"""

#Calculator
"""
while True:
	try:
		num1 = int(input("Enter number 1: "))
		num2 = int(input("Enter number 2: "))

		#Asking for the operation
		user_op = input("Please choose the operation you would like to use (add, subtract, multiply, divide): ")

		# Perform the chosen operation
		if user_op.lower() == "add":
			value = num1 + num2
			print(f"The value is {value}")
		elif user_op.lower() == "subtract":
			value = num1 - num2
			print(f"The value is {value}")
		elif user_op.lower() == "multiply":
			value = num1 * num2
			print(f"The value is {value}")
		elif user_op.lower() == "divide":
			if num2 == 0:
				print("Error: Cannot divide by 0")
				continue
			value = num1 / num2
			print(f"The value is {value}")
		else:
			print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
			continue

		# Asking if they want another calculation
		choice = input("\nWould you like to perform another calculation? (yes or no): ")
		if choice == "no":
			print("\n**********************************")
			print("Thank you for using the calculator")
			print("**********************************")
			break
	except ValueError:
		print("Invalid input, Please enter a valid number (non negative)")
"""

#Functions
"""
def sqr_number(num1):
	result = num1 ** 2
	return result

#Calling the function
user_input = int(input("Enter a number: "))
value = sqr_number(user_input)
print(value)
"""
def calculate_bmi(weight, height):
	result = weight / (height ** 2)
	return(result)

#Calling the function
weight = int(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))
value = calculate_bmi(weight, height)

# Print the BMI value rounded to 2 decimal places
print(f"Your BMI is: {value:.2f}")

#Classity the BMI
if value <18.5:
	print("Underweight")
elif 18.5 <= value < 24.9:
	print("Normal Weight")
elif 25 <= value < 29.9:
	print("Overweight")
else:
	print("Obesity")