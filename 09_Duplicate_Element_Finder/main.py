# Topics: lists, sets, loops, membership checks and conditions.
raw = input("Enter integers separated by spaces: ")
parts = raw.split()
numbers = []
for item in parts:
    numbers.append(int(item))

seen = set()
duplicates = set()
for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

if len(duplicates) > 0:
    duplicate_list = list(duplicates)
    duplicate_list.sort()
    print("Duplicate values:", duplicate_list)
else:
    print("No duplicate values found.")
