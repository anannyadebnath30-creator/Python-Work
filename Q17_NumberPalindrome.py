n = int(input("Enter an integer: "))
original = abs(n)
temp = original
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
