#Day3
#Challenge 1
"""
fruits = ["mango", "pear", "banana", "apple", "cherry"]
print(fruits[2])
fruits.append("orange")
fruits.append("guava")
fruits.remove("mango")
print(fruits)
"""

#Challenge 2
"""
grocery_items = ["bread", "jam", "butter", "water", "tissue"]
print("Current grocery list: ", grocery_items)
user_items = input("Enter 2 items separated by spaces: ").lower()
new_items = user_items.split()
grocery_items.extend(new_items)
print("Updated grocery list after adding items: ", grocery_items)
item_remove = input("Enter item to remove: ").lower()
if item_remove in grocery_items:
	grocery_items.remove(item_remove)
	print("updated grocery list after removing item: ", grocery_items)
else:
	print(f"'{item_remove}' not found in list.")
grocery_items.sort()
print(grocery_items)
"""

#Dictionaries
#Excercise 1
"""
book = {
	"title": None,
	"author": None,
	"year": None
}

book["title"] = input("Enter a title: ")
book["author"] = input("Enter an author: ")
try:
	book["year"] = int(input("Enter a year: "))
except ValueError:
	print("Invalid Year! Please enter a valid number for year")

print(book)
"""

#Challenge 1
"""
student_grade = {
	"name": None,
	"age": None,
	"subject": None,
	"grade": None
}

student_grade["name"] = input("Enter the student's name: ")
student_grade["age"] = int(input("Enter the student's age: "))
student_grade["subject"] = input("Enter a subject: ")
student_grade["grade"] = int(input("Enter a number grade: "))

print(student_grade)

update = input("Do you want to update your grade? (yes/no): ").lower()
if update == "yes":
	student_grade["grade"] = int(input("Enter the new grade: "))
	print("Grade Updated!")
else:
	print("Grade remains the same")

print(student_grade)
"""

#Challenge 2
"""
students = {
	"Student_1": {
	"name": "Samantha",
	"age": 32,
	"subjects": ["math", "english"],
	"grade": "A"
	},
	"Student_2": {
	"name": "Nicheal",
	"age": 33,
	"subjects": ["science", "music"],
	"grade": "B"
	}
}
print(students)

update = input("Do you want to update your grade? (yes/no): ").lower()
if update == "yes":
	student_choice = input("Choose student (first/second: ").lower()
	if student_choice == "first":
		students["Student_1"]["grade"] = input("Enter the new grade: ")
		print("Grade Updated!")
	elif student_choice == "second":
		students["Student_2"]["grade"] = input("Enter the new grade: ")
		print("Grade Updated!")
	else:
		print("Invalid choice. Please select from 'first' or 'second")
else:
	print("Grade remains the same")

print(students)
"""

#Challenge 3
"""
items = ["pen", "notebook", "pen", "eraser", "pencil", "notebook", "pencil", "pencil", "pen", "eraser", "notebook"]
count = {}
for item in items:
	if item in count:
		count[item] += 1
	else:
		count[item] = 1

for key, value in count.items():
	print(f"{key}: {value}")
"""