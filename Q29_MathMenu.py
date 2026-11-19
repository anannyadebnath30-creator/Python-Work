def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    text = str(abs(n))
    return text == text[::-1]

def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    return sum(int(digit) ** len(digits) for digit in digits) == n

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n < 0:
        return None
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

while True:
    print("\\n--- MATHEMATICAL MENU ---")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "6":
        print("Goodbye!")
        break
    elif choice in ("1", "2", "3", "4"):
        n = int(input("Enter an integer: "))
        if choice == "1":
            print("Prime" if is_prime(n) else "Not prime")
        elif choice == "2":
            print("Palindrome" if is_palindrome(n) else "Not palindrome")
        elif choice == "3":
            print("Armstrong" if is_armstrong(n) else "Not Armstrong")
        else:
            result = factorial(n)
            print("Factorial =", result if result is not None else "not defined for negative integers")
    elif choice == "5":
        terms = int(input("Enter number of terms: "))
        result = fibonacci(terms)
        print("Fibonacci series =", result if result is not None else "enter a non-negative number")
    else:
        print("Invalid choice. Please try again.")
