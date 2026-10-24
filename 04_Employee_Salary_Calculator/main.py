basic = float(input("Enter basic salary (Rs.): "))
if basic < 0:
    print("Salary cannot be negative.")
else:
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    print(f"Basic salary: Rs. {basic:.2f}")
    print(f"HRA (20%): Rs. {hra:.2f}")
    print(f"DA (10%): Rs. {da:.2f}")
    print(f"Gross salary: Rs. {gross:.2f}")
