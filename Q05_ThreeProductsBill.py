# Sample rules: 10% discount when subtotal is Rs. 1000 or more; GST is 18%.
subtotal = 0
for i in range(1, 4):
    price = float(input(f"Enter price of product {i}: Rs. "))
    quantity = int(input(f"Enter quantity of product {i}: "))
    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        raise SystemExit
    subtotal += price * quantity

discount = subtotal * 0.10 if subtotal >= 1000 else 0
taxable_amount = subtotal - discount
gst = taxable_amount * 0.18
final_amount = taxable_amount + gst

print(f"Subtotal = Rs. {subtotal:.2f}")
print(f"Discount = Rs. {discount:.2f}")
print(f"GST (18%) = Rs. {gst:.2f}")
print(f"Final payable amount = Rs. {final_amount:.2f}")
