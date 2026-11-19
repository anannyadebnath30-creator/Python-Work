# Sample slabs (replace rates if your college specifies different rates):
# First 100 units: Rs. 1.50/unit; next 100: Rs. 2.50/unit;
# next 200: Rs. 4/unit; above 400: Rs. 6/unit.
units = float(input("Enter electricity units consumed: "))
if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 400:
        bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        bill = 100 * 1.50 + 100 * 2.50 + 200 * 4.00 + (units - 400) * 6.00
    print(f"Electricity bill = Rs. {bill:.2f}")
