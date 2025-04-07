def get_student_info():
	student_info = {
	#Collecting User Info
		"name": input("Enter student name: "),
		"age": int(input("Enter student age: ")),
		"grades": []
	}

	num_subjects = int(input("Enter the amount of subjects: "))

	#Collecting grades for each subject
	for i in range(num_subjects):
		new_subject = input(f"Enter the name of the subject {i + 1}: ")
		grade = input(f"Enter the letter grade for {new_subject}: ").upper()

		#ensure valid grade input
		while grade not in ["A", "B", "C", "D", "F"]:
			print("Invalid grade. Please enter a grade from A, B, C, D, F.")
			grade = input(f"Enter the letter grade for {new_subject}: ").upper()

		student_info["grades"].append({
			"subject": new_subject,
			"grade": grade
			})
	return student_info

def total_and_average(grades, num_subjects):
	grade_points = {
		"A": 4,
		"B": 3,
		"C": 2,
		"D": 1,
		"F": 0
	}

	total = 0
	for entry in grades:
		letter = entry["grade"]
		numerical_grade = grade_points[letter]
		total += numerical_grade

	average = total / num_subjects
	return total, average

def display_student_summary(student_info, total, average):
	print("\nStudent Information Summary:")
	print("Name:", student_info["name"])
	print("Age:", student_info["age"])
	print("Subjects and Grades:")
	for subject in student_info["grades"]:
		print(f"- {subject['subject']}: {subject['grade']}")
	print(f"Total Points: {total}")
	print(f"Average: {average:.2f}")

def main():
	while True:
		student_info = get_student_info()
		total, average = total_and_average(student_info["grades"], len(student_info["grades"]))
		display_student_summary(student_info, total, average)

		#Ask if user wants to enter another student
		again = input("\nDo you want to enter another student's data? (yes/no): ").lower()
		if again != "yes":
			print("Goodbye!")
			break

if __name__ == "__main__":
	main()