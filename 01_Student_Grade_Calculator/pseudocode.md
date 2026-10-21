# Pseudocode

BEGIN
    INPUT student_name
    INPUT mark1, mark2, mark3
    IF any mark < 0 OR any mark > 100 THEN
        DISPLAY "Invalid marks"
    ELSE
        total = mark1 + mark2 + mark3
        average = total / 3
        IF average >= 90 THEN grade = "A"
        ELSE IF average >= 80 THEN grade = "B"
        ELSE IF average >= 70 THEN grade = "C"
        ELSE IF average >= 60 THEN grade = "D"
        ELSE IF average >= 40 THEN grade = "E"
        ELSE grade = "F"
        DISPLAY total, average, grade
        IF average >= 40 THEN DISPLAY "PASS"
        ELSE DISPLAY "FAIL"
    END IF
END
