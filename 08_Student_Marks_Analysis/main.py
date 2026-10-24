marks = []
count = int(input("Enter number of students: "))
if count <= 0:
    print("Number of students must be positive.")
else:
    for i in range(count):
        mark = float(input(f"Enter marks for student {i + 1} (0-100): "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            break
        marks.append(mark)
    else:
        passed = 0
        for mark in marks:
            if mark >= 40:
                passed += 1
        print(f"Average: {sum(marks) / len(marks):.2f}")
        print(f"Highest: {max(marks):.2f}")
        print(f"Lowest: {min(marks):.2f}")
        print(f"Passed: {passed}")
