# Q2. File handling: write, read, append, line-by-line
filename = "student.txt"
name = input("Enter student name: ")
roll = input("Enter roll number: ")
with open(filename, "w") as file:
    file.write(f"Name: {name}, Roll: {roll}\n")
print("Initial file contents:")
with open(filename, "r") as file:
    print(file.read())
more_name = input("Enter another student name to append: ")
more_roll = input("Enter their roll number: ")
with open(filename, "a") as file:
    file.write(f"Name: {more_name}, Roll: {more_roll}\n")
print("Reading file line by line:")
file = open(filename, "r")
for line in file:
    print(line.rstrip())
file.seek(0)
print("All lines:", file.readlines())
file.close()
print("File closed:", file.closed)
