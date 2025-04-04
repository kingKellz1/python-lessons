#Tuples
#simple example of extracting information from a tuple
"""
person = ("Kai", 24, "Jamaica")
name, age, country = person
print(name)    # Kai
print(age)     # 24
print(country) # Jamaica

car = ("BMW", "X650i", "2023")
make, model, year = car
print(make)
print(model)
print(year)
"""
"""
x = ("banana", "apple", "pear", "cherry", "guava", 2, 3, 4, 3, 4, 3, 5, 1)
print(x.count(3))
print(x.index("guava"))
x[1] = "orange"
"""
"""
x = ("banana", "apple", "pear")
temp_list = list(x)  # Convert tuple to list
temp_list[1] = "orange"  # Modify the list
x = tuple(temp_list)  # Convert list back to tuple
print(x)
"""

#Challenge 1: Manipulate Tuples with Functions
"""
Steps:
Define a function called modify_tuple.
Loop through the tuple to check each number.
Apply the respective modification (double for even, triple for odd).
Return a new tuple with the modified values.
"""

"""
def modify_tuple(my_num):
	new_num = []
	for num in my_num:
		if num % 2 == 0:
			new_num.append(num * 2) #Even: double the number
		else:
			new_num.append(num * 3) #Odd: triple the number
	return tuple(new_num)

u_num = (4, 5, 6, 7, 8)
result = modify_tuple(u_num)
print(result)
"""
#Challenge 2: Count Occurrences of Elements in a List
"""
Steps:
Create an empty dictionary.
Loop through the list of items.
Check if the item already exists in the dictionary:
If it does, increment its value by 1.
If it doesn’t, add it to the dictionary with a value of 1.
Print the dictionary showing the count of each item.
"""

"""
my_dict = {}
items = ["pen", "notebook", "pen", "eraser", "pencil", "notebook", "pencil", "pencil", "pen", "eraser", "notebook"]
for item in items:
	if item in my_dict:
		my_dict[item] += 1
	else:
		my_dict[item] = 1
print(my_dict)
"""

#Challenge 3: Nested Dictionaries and Lists
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

#Challenge 4: Nesting Dictionaries
"""
Create a dictionary called inventory that contains products as keys, with the following information as values:

Name of the product
Price of the product
Quantity in stock
Once the dictionary is created, print out:

The name, price, and quantity of each product.
The total cost of each product (Price * Quantity).
The total inventory cost (sum of all total costs).
"""

"""
inventory = {
	"apple": {"name": "Apple", "price": 0.5, "quantity": 30},
    "banana": {"name": "Banana", "price": 0.3, "quantity": 50},
    "cherry": {"name": "Cherry", "price": 1.2, "quantity": 20}
}

#My initial Code

for product, details in inventory.items():
    name = details["name"]
    price = details["price"]
    quantity = details["quantity"]

    
    # Print the product details
    print(f"Product: {name}, Price: ${price}, Quantity: {quantity}")

apple_price = inventory["apple"]["price"]
apple_quantity = inventory["apple"]["quantity"]
total_cost_apple = apple_price * apple_quantity

banana_price = inventory["banana"]["price"]
banana_quantity = inventory["banana"]["quantity"]
total_cost_banana = banana_price * banana_quantity

cherry_price = inventory["cherry"]["price"]
cherry_quantity = inventory["cherry"]["quantity"]
total_cost_cherry = cherry_price * cherry_quantity
total_inventory_cost = total_cost_apple + total_cost_banana + total_cost_cherry

print("\nThe total price of apple is: $", total_cost_apple)
print("The total price of banana is: $", total_cost_banana)
print("The total price of cherry is: $", total_cost_cherry)
print("The total inventory cost is: $", total_inventory_cost)

#My updated code

total_inventory_cost = 0

for product, details in inventory.items():
    total_cost = details["price"] * details["quantity"]
    total_inventory_cost += total_cost
    print(f"Product: {details['name']}, Price: ${details['price']}, Quantity: {details['quantity']}, Total Cost: ${total_cost}")

print("\nThe total inventory cost is: $", total_inventory_cost)
"""

#Challenge 5: Merging Two Dictionaries
"""
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 4, "b": 5, "d": 6}

# Your task is to merge dict1 and dict2
# If there are duplicate keys, sum their values

result = {}  # New dictionary to store the result

# Write your solution here
for key, value in dict1.items():
	result[key] = value
for key, value in dict2.items():
	if key in result:
		result[key] += value
	else:
		result[key] = value

print(result)
"""

def find_largest(numbers):
	largest = numbers[0]
	for num in numbers[1:]:
		if num > largest:
			largest = num
	return largest

numbers = [5, 1, 8, 3, 12, 9]
result = find_largest(numbers)
print("The largest number is:", result)
