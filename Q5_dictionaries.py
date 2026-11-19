# Q5. Dictionaries, dictionary comprehension and nested collections
employees = {
    1001: {"name": "Asha", "department": "IT", "salary": 45000},
    1002: {"name": "Rahul", "department": "HR", "salary": 35000},
    1003: {"name": "Meera", "department": "Finance", "salary": 52000}
}
print("Employees:", employees)
employees[1004] = {"name": "Karan", "department": "IT", "salary": 40000}  # Add
employees[1002]["salary"] = 38000  # Update
employees[1003]["department"] = "Accounts"
print("After adding/updating:", employees)
remove_id = int(input("Employee ID to delete (0 to skip): "))
if remove_id in employees and remove_id != 0:
    del employees[remove_id]
print("Employee IDs:", employees.keys())
print("Employee records:", employees.values())
print("Employee key-value pairs:")
for emp_id, details in employees.items():
    print(emp_id, details)
search_id = int(input("Enter employee ID to search: "))
if search_id in employees:
    print("Found:", employees[search_id])
else:
    print("Employee not found")
limit = float(input("Salary threshold: "))
high_salary = {emp_id: details for emp_id, details in employees.items() if details["salary"] > limit}
print("Employees earning above threshold:", high_salary)
