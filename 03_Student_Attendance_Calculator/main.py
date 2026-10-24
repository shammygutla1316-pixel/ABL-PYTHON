# Topics: input/output, type conversion, arithmetic, comparisons, selection.
held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
if held <= 0:
    print("Total classes held must be positive.")
elif attended < 0 or attended > held:
    print("Attended classes must be between 0 and total classes.")
else:
    percentage = attended / held * 100
    print("Attendance:", format(percentage, ".2f") + "%")
    if percentage >= 75:
        print("Status: Eligible")
    else:
        print("Status: Shortage")
