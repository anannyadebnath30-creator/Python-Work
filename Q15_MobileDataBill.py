# Example slabs: up to 2 GB Rs. 100; >2 to 5 GB Rs. 200;
# >5 to 10 GB Rs. 350; above 10 GB Rs. 500.
usage = float(input("Enter monthly data usage in GB: "))
if usage < 0:
    print("Usage cannot be negative.")
elif usage <= 2:
    bill = 100
elif usage <= 5:
    bill = 200
elif usage <= 10:
    bill = 350
else:
    bill = 500
if usage >= 0:
    print(f"Monthly data bill = Rs. {bill:.2f}")
