# Q3. Recursive factorial and Fibonacci series

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    series = fibonacci(n - 1)
    next_value = 0 if len(series) < 2 else series[-1] + series[-2]
    if len(series) == 1:
        next_value = 1
    series.append(next_value)
    return series

num = int(input("Enter a number for factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(num))
terms = int(input("Enter number of Fibonacci terms: "))
print("Fibonacci series:", fibonacci(terms))
