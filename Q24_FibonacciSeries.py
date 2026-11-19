terms = int(input("Enter number of Fibonacci terms: "))
if terms < 0:
    print("Number of terms cannot be negative.")
else:
    a, b = 0, 1
    series = []
    for _ in range(terms):
        series.append(a)
        a, b = b, a + b
    print("Fibonacci series:", series)
    print("Sum of terms =", sum(series))
