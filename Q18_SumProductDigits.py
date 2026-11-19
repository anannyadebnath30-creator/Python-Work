n = abs(int(input("Enter an integer: ")))
if n == 0:
    digit_sum = 0
    digit_product = 0
else:
    digit_sum = 0
    digit_product = 1
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_product *= digit
        n //= 10

print("Sum of digits =", digit_sum)
print("Product of digits =", digit_product)
