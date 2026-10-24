# Topics: lists, loops, input/output, arithmetic and selection.
marks = []
count = int(input("Enter number of students: "))
valid = True

if count <= 0:
    print("Number of students must be positive.")
else:
    for i in range(count):
        mark = float(input("Enter marks for student " + str(i + 1) + " (0-100): "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            valid = False
            break
        marks.append(mark)

    if valid:
        total = 0
        highest = marks[0]
        lowest = marks[0]
        passed = 0
        for mark in marks:
            total = total + mark
            if mark > highest:
                highest = mark
            if mark < lowest:
                lowest = mark
            if mark >= 40:
                passed = passed + 1
        average = total / len(marks)
        print("Average:", format(average, ".2f"))
        print("Highest:", format(highest, ".2f"))
        print("Lowest:", format(lowest, ".2f"))
        print("Passed:", passed)
