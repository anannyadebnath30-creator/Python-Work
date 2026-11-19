start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
if start > end:
    start, end = end, start

primes = []
for n in range(max(2, start), end + 1):
    is_prime = True
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)

print("Prime numbers:", primes)
print("Total prime numbers =", len(primes))
