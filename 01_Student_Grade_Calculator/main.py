"""Project 1: Student Marks and Grade Calculator.
Syllabus: input/output, type conversion, arithmetic, operators, if-elif-else.
"""
student_name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

if (mark1 < 0 or mark1 > 100 or
        mark2 < 0 or mark2 > 100 or
        mark3 < 0 or mark3 > 100):
    print("Invalid marks. Each mark must be between 0 and 100.")
else:
    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    print("\n--- Student Result ---")
    print("Student Name:", student_name)
    print("Total Marks:", format(total, ".2f"), "/ 300")
    print("Average:", format(average, ".2f"), "%")
    print("Grade:", grade)
    if average >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")
