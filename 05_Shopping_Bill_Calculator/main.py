prices = []
for i in range(1, 4):
    price = float(input(f"Enter price of item {i} (Rs.): "))
    if price < 0:
        print("Price cannot be negative.")
        break
    prices.append(price)
else:
    subtotal = sum(prices)
    discount = subtotal * 0.10 if subtotal >= 1000 else 0
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"Final amount: Rs. {subtotal - discount:.2f}")
