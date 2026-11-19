percentage = float(input("Enter percentage (0-100): "))
if not 0 <= percentage <= 100:
    print("Invalid percentage. Enter a value from 0 to 100.")
elif percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 40:
    print("Grade: E")
else:
    print("Grade: F (Fail)")
