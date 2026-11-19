# Example criteria: at least 60 in each subject and 70% overall average.
maths = float(input("Enter Mathematics marks out of 100: "))
physics = float(input("Enter Physics marks out of 100: "))
chemistry = float(input("Enter Chemistry marks out of 100: "))

if any(mark < 0 or mark > 100 for mark in (maths, physics, chemistry)):
    print("Invalid marks. Each mark must be between 0 and 100.")
else:
    overall_percentage = (maths + physics + chemistry) / 3
    if maths >= 60 and physics >= 60 and chemistry >= 60 and overall_percentage >= 70:
        print(f"Eligible for admission. Overall = {overall_percentage:.2f}%")
    else:
        print(f"Not eligible for admission. Overall = {overall_percentage:.2f}%")
