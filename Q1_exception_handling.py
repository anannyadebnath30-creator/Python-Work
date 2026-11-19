# Q1. Exception handling examples
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    print("Division:", numerator / denominator)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print("No exception occurred in the division operation.")
finally:
    print("Division attempt finished.")

items = [10, 20, 30]
try:
    index = int(input("Enter a list index (0-2): "))
    print("Selected item:", items[index])
except ValueError:
    print("Please enter an integer index.")
except IndexError:
    print("Invalid index. The list has only three items.")
finally:
    print("List access attempt finished.")

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Age accepted.")
except ValueError as error:
    print("Age error:", error)
