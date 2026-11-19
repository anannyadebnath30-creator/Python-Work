n = int(input("Enter an integer: "))
if n == 0:
    print("The number is zero.")
else:
    if n > 0:
        print("Positive")
    else:
        print("Negative")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
