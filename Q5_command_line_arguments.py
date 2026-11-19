# Q5. Arithmetic using command-line arguments
# Example: python Q5_command_line_arguments.py 12 4 +
import sys

if len(sys.argv) != 4:
    print("Usage: python Q5_command_line_arguments.py <number1> <number2> <operator>")
    print("Example: python Q5_command_line_arguments.py 12 4 +")
else:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        operator = sys.argv[3]
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError("Unsupported operator. Use +, -, *, or /.")
        print("Result:", result)
    except ValueError as error:
        print("Input error:", error)
    except ZeroDivisionError as error:
        print("Math error:", error)
