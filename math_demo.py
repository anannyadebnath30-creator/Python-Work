# Q4.1 math library demonstration
import math
number = float(input("Enter a number: "))
if number >= 0:
    print("Square root:", math.sqrt(number))
else:
    print("Square root of a negative number is not real.")
integer = int(input("Enter a non-negative integer for factorial: "))
if integer >= 0:
    print("Factorial:", math.factorial(integer))
else:
    print("Factorial requires a non-negative integer.")
base = float(input("Enter base: "))
exponent = float(input("Enter exponent: "))
print("Power:", math.pow(base, exponent))
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))
