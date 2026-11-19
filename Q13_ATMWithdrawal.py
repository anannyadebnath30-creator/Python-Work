# Demo PIN only; never store real PINs directly in a program.
correct_pin = "1234"
entered_pin = input("Enter your 4-digit PIN: ")
balance = float(input("Enter account balance: Rs. "))
amount = float(input("Enter withdrawal amount: Rs. "))

if entered_pin != correct_pin:
    print("Incorrect PIN.")
elif amount <= 0:
    print("Withdrawal amount must be positive.")
elif amount > balance:
    print("Insufficient balance.")
else:
    balance -= amount
    print("Withdrawal successful.")
    print(f"Remaining balance = Rs. {balance:.2f}")
