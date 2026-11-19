# Q2. String slicing and formatting
full_name = input("Enter full name: ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter mobile number: ").strip()
parts = full_name.split()
first_name = parts[0] if parts else ""
last_name = parts[-1] if parts else ""
username, domain = email.split("@", 1) if "@" in email else (email, "Invalid email")
print("First name:", first_name)
print("Last name:", last_name)
print("Name reversed:", full_name[::-1])
print("Email username:", username)
print("Email domain:", domain)
print("Last four mobile digits:", mobile[-4:])
print(f"Student: {full_name} | Email: {email} | Mobile: {mobile}")
print("Using format(): Student {} has email {}".format(full_name, email))
print("Positive indexing (first character):", full_name[0] if full_name else "N/A")
print("Negative indexing (last character):", full_name[-1] if full_name else "N/A")
