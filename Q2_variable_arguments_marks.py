# Q2. Variable-length arguments and return statement

def student_result(name, *marks, **details):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    highest = max(marks) if marks else 0
    return total, average, highest, name, details



name = input("Enter student name: ")
marks = [float(x) for x in input("Enter marks separated by spaces: ").split()]
roll = input("Enter roll number: ")
class_name = input("Enter class: ")
result = student_result(name, *marks, roll_number=roll, class_name=class_name)
total, average, highest, student_name, info = result
print("\n--- Student Result ---")
print(f"Name: {student_name}")
print(f"Roll Number: {info['roll_number']}")
print(f"Class: {info['class_name']}")
print(f"Total Marks: {total:.2f}")
print(f"Average Marks: {average:.2f}")
print(f"Highest Marks: {highest:.2f}")
