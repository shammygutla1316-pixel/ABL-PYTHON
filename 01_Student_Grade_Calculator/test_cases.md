# Test Cases

| Test | Marks | Expected result |
|---|---|---|
| 1 | 95, 90, 85 | Average 90; Grade A; PASS |
| 2 | 75, 70, 65 | Average 70; Grade C; PASS |
| 3 | 30, 35, 40 | Average 35; Grade F; FAIL |
| 4 | -5, 80, 70 | Invalid marks message |
| 5 | 100, 100, 100 | Average 100; Grade A; PASS |

## Sample run

```text
Enter student name: Ravi
Enter marks for Subject 1 (0-100): 95
Enter marks for Subject 2 (0-100): 90
Enter marks for Subject 3 (0-100): 85

--- Student Result ---
Student Name: Ravi
Total Marks: 270.00 / 300
Average: 90.00 %
Grade: A
Result: PASS
```

Run the program yourself and save screenshots in the `output/` folder.
