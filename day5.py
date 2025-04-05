#Day 5: Functions, Loops, and Intro to File Handling

#1. Functions Recap & Arguments
"""
def greet_user(user, time):
	print(f"Good {time}, {user}! Welcome back.")

user = input("Enter your name: ")
time = input("Is it (morning, noon, afternoon or night): ")
greet_user(user, time)
"""

#2. Functions with Loops
"""
def check_even_odd(numbers):
	for num in numbers:
		if num % 2 == 0:
			print(f"{num} is even")
		else:
			print(f"{num} is odd")

check_even_odd([1, 4, 7, 10, 15])
"""

#Quick Challenge: Sum Only the Even Numbers
"""
def sum_even(numbers):
	count = 0
	for num in numbers:
		if num % 2 == 0:
			count += num
	return count

result = sum_even([2, 5, 8, 11, 14])
print("Sum of even numbers:", result)
"""

#Challenge:
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_num = [num * 2 for num in list_1 if num % 2 == 0]
print(new_num)
"""
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_num = []
for num in list_1:
	if num % 2 == 0:
		new_num.append(num * 2)
print(new_num)
"""