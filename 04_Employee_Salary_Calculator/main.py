# Topics: variables, numeric input, arithmetic operators, output formatting, selection.
# Allowance percentages are illustrative classroom assumptions.
basic = float(input("Enter basic salary (Rs.): "))
if basic < 0:
    print("Salary cannot be negative.")
else:
    hra = basic * 20 / 100
    da = basic * 10 / 100
    gross = basic + hra + da
    print("Basic salary: Rs.", format(basic, ".2f"))
    print("HRA (20%): Rs.", format(hra, ".2f"))
    print("DA (10%): Rs.", format(da, ".2f"))
    print("Gross salary: Rs.", format(gross, ".2f"))
