raw = input("Enter integers separated by spaces: ").split()
numbers = [int(item) for item in raw]
seen = set()
duplicates = set()
for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)
if duplicates:
    print("Duplicate values:", sorted(duplicates))
else:
    print("No duplicate values found.")
