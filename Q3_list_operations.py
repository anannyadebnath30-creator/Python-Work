# Q3. List operations and list comprehension
numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
print("Original list:", numbers)
value = int(input("Number to insert: "))
position = int(input("Position (0-based index): "))
numbers.insert(max(0, min(position, len(numbers))), value)
print("After insert:", numbers)
remove_value = int(input("Value to remove (if present): "))
if remove_value in numbers:
    numbers.remove(remove_value)
else:
    print("Value not found.")
print("After remove:", numbers)
ascending = sorted(numbers)
print("Ascending:", ascending)
print("Descending:", sorted(numbers, reverse=True))
if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))
print("Concatenation:", numbers + [100, 200])
print("Repetition:", numbers * 2)
print("First element:", numbers[0] if numbers else "Empty list")
search = int(input("Number to search: "))
print("Membership:", search in numbers)
print("Even numbers:", [n for n in numbers if n % 2 == 0])
print("Odd numbers:", [n for n in numbers if n % 2 != 0])
print("Squares:", [n ** 2 for n in numbers])
# Demonstrate append, extend, pop, sort and reverse methods
numbers.append(50)
numbers.extend([60, 70])
if numbers:
    numbers.pop()
numbers.sort()
numbers.reverse()
print("List after append/extend/pop/sort/reverse:", numbers)
