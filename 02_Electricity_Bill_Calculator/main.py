# Topics: input/output, type conversion, arithmetic, if-elif-else.
# Slab rates are illustrative classroom values.
units = float(input("Enter electricity units consumed: "))
if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00
    print("Units consumed:", format(units, ".1f"))
    print("Estimated bill: Rs.", format(bill, ".2f"))
