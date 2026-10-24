# Topics: lists, loops, input/output, arithmetic and if-else.
prices = []
valid = True
for i in range(1, 4):
    price = float(input("Enter price of item " + str(i) + " (Rs.): "))
    if price < 0:
        print("Price cannot be negative.")
        valid = False
        break
    prices.append(price)

if valid:
    subtotal = 0
    for price in prices:
        subtotal = subtotal + price
    if subtotal >= 1000:
        discount = subtotal * 10 / 100
    else:
        discount = 0
    total = subtotal - discount
    print("Subtotal: Rs.", format(subtotal, ".2f"))
    print("Discount: Rs.", format(discount, ".2f"))
    print("Final amount: Rs.", format(total, ".2f"))
