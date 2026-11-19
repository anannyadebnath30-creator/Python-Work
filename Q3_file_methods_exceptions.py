# Q3. File methods and file-related exception handling
filename = input("Enter file name to read (e.g., student.txt): ")
try:
    file = open(filename, "r")
    print("File name:", file.name)
    print("File mode:", file.mode)
    print("read() result:")
    print(file.read())
    print("Position after read:", file.tell())
    file.seek(0)
    print("First line using readline():")
    print(file.readline())
    file.seek(0)
    print("All lines using readlines():")
    print(file.readlines())
except FileNotFoundError:
    print("Error: File does not exist.")
except PermissionError:
    print("Error: Permission denied.")
except OSError as error:
    print("File error:", error)
else:
    print("File was read successfully.")
finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("No file was opened.")
    except Exception:
        pass
