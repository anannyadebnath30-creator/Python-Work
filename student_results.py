# Student result module

def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average

def display_result(marks):
    total, average = calculate_result(marks)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
