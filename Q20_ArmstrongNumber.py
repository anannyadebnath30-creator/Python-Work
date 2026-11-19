n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    digits = len(str(n))
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    # For n = 0, the sum is also zero.
    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
