# Q4.3 datetime library demonstration
from datetime import datetime, date
now = datetime.now()
print("Current date and time:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
first_date = date.fromisoformat(input("Enter first date (YYYY-MM-DD): "))
second_date = date.fromisoformat(input("Enter second date (YYYY-MM-DD): "))
difference = abs(second_date - first_date)
print("Difference between dates:", difference.days, "days")
