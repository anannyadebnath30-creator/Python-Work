# Example annual tax slabs; replace with the slabs in your assignment.
income = float(input("Enter annual income: Rs. "))
if income < 0:
    print("Income cannot be negative.")
else:
    # Progressive example: 0% up to Rs. 2,50,000;
    # 5% on next Rs. 2,50,000; 10% on next Rs. 5,00,000;
    # 20% above Rs. 10,00,000.
    tax = 0
    if income > 250000:
        tax += (min(income, 500000) - 250000) * 0.05
    if income > 500000:
        tax += (min(income, 1000000) - 500000) * 0.10
    if income > 1000000:
        tax += (income - 1000000) * 0.20
    print(f"Tax payable = Rs. {tax:.2f}")
