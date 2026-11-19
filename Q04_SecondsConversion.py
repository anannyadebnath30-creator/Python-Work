seconds = int(input("Enter duration in seconds: "))
if seconds < 0:
    print("Duration cannot be negative.")
else:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"{hours} hour(s), {minutes} minute(s), {remaining_seconds} second(s)")
