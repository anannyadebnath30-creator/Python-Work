# Example rates: DA 10%, HRA 20%, tax 5% of gross salary.
basic = float(input("Enter basic salary: Rs. "))
da = basic * 0.10
hra = basic * 0.20
gross = basic + da + hra
tax = gross * 0.05
net = gross - tax

print(f"DA = Rs. {da:.2f}")
print(f"HRA = Rs. {hra:.2f}")
print(f"Gross salary = Rs. {gross:.2f}")
print(f"Tax deduction = Rs. {tax:.2f}")
print(f"Net salary = Rs. {net:.2f}")
