n = int(input("Enter number of rows: "))
if n <= 0:
    print("Enter a positive number of rows.")
else:
    # Example pattern:
    # 1
    # 1 2
    # 1 2 3
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
