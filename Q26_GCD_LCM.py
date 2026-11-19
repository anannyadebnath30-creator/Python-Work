a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
if a <= 0 or b <= 0:
    print("Both numbers must be positive.")
else:
    original_a, original_b = a, b
    while b != 0:
        a, b = b, a % b
    gcd = a
    lcm = (original_a * original_b) // gcd
    print("GCD =", gcd)
    print("LCM =", lcm)
