# Topics: loops, nested loops, conditions and pattern generation.
rows = int(input("Enter number of rows (1-20): "))
if rows < 1 or rows > 20:
    print("Rows must be between 1 and 20.")
else:
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()
