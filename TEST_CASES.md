# Consolidated Test Cases — Python ABL Projects

These are expected-output checks for the sample programs. Run each project from its own folder using Python 3. Inputs are shown in the order requested by the prompts. Illustrative thresholds and rates are classroom assumptions.

## 1. Student Marks and Grade Calculator
See [project test cases](01_Student_Grade_Calculator/test_cases.md).

## 2. Electricity Bill Calculator
| Input units | Expected result |
|---:|---|
| 50 | Estimated bill: Rs. 75.00 |
| 150 | Estimated bill: Rs. 275.00 |
| 250 | Estimated bill: Rs. 650.00 |
| 350 | Estimated bill: Rs. 1,250.00 |
| -2 | Units cannot be negative. |

## 3. Student Attendance Calculator
| Total classes; attended | Expected result |
|---|---|
| 100; 80 | Attendance: 80.00%; Eligible |
| 100; 75 | Attendance: 75.00%; Eligible |
| 100; 60 | Attendance: 60.00%; Shortage |
| 0; 0 | Total classes held must be positive. |
| 10; 12 | Invalid attended-class count message |

## 4. Employee Salary Calculator
| Basic salary | Expected result |
|---:|---|
| 10000 | Gross salary: Rs. 13000.00 |
| 25000 | Gross salary: Rs. 32500.00 |
| 0 | Gross salary: Rs. 0.00 |
| -1 | Salary cannot be negative. |

## 5. Shopping Bill Calculator
| Item prices | Expected result |
|---|---|
| 200, 300, 400 | Subtotal Rs. 900.00; discount Rs. 0.00; final Rs. 900.00 |
| 500, 300, 400 | Subtotal Rs. 1200.00; discount Rs. 120.00; final Rs. 1080.00 |
| -1 as first price | Price cannot be negative. |

## 6. Number Guessing Game
| Guesses | Expected result |
|---|---|
| 37 | Correct! You guessed the number. |
| 20, 40, 37 | Too low; too high; correct |
| 1, 2, 3, 4, 5 | Game over. The number was 37. |

## 7. Basic Password Checker
| Password | Expected result |
|---|---|
| Abcdef12 | Password meets the basic rules. |
| abcdef12 | Rejected: uppercase letter missing |
| ABCD1234 | Rejected: lowercase letter missing |
| Abcdefgh | Rejected: digit missing |
| Ab1 | Rejected: fewer than 8 characters |

## 8. Student Marks Analysis
| Number of students; marks | Expected result |
|---|---|
| 4; 70, 80, 30, 100 | Average 70.00; highest 100.00; lowest 30.00; passed 3 |
| 3; 40, 40, 40 | Average 40.00; highest 40.00; lowest 40.00; passed 3 |
| 0 | Number of students must be positive. |
| 1; 101 | Marks must be between 0 and 100. |

## 9. Duplicate Element Finder
| Input sequence | Expected result |
|---|---|
| 1 2 3 2 4 1 | Duplicate values: [1, 2] |
| 5 5 5 | Duplicate values: [5] |
| 1 2 3 | No duplicate values found. |
| Empty input | No duplicate values found. |

## 10. Pattern Printing
| Rows | Expected result |
|---:|---|
| 4 | `*`, `**`, `***`, `****` on separate lines |
| 1 | `*` |
| 0 | Rows must be between 1 and 20. |
| 21 | Rows must be between 1 and 20. |

## Screenshot evidence
Screenshots should show actual program execution, including the entered test values and resulting output. Store verified screenshots in each project's `output/` folder. Do not label expected-output tables as screenshots.
