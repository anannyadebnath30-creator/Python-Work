n = int(input("Enter number of students: "))
if n <= 0:
    print("Number of students must be positive.")
else:
    marks = []
    for i in range(1, n + 1):
        mark = float(input(f"Enter marks for student {i} (out of 100): "))
        if not 0 <= mark <= 100:
            print("Invalid mark. Enter a value between 0 and 100.")
            raise SystemExit
        marks.append(mark)

    average = sum(marks) / n
    highest = max(marks)
    lowest = min(marks)
    passed = sum(1 for mark in marks if mark >= 40)
    failed = n - passed
    above_75 = sum(1 for mark in marks if mark > 75)

    print(f"Class average = {average:.2f}")
    print("Highest marks =", highest)
    print("Lowest marks =", lowest)
    print("Passed students =", passed)
    print("Failed students =", failed)
    print("Students scoring above 75% =", above_75)
