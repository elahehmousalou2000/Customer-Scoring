def customer_score(purchases, spending):
    return round(purchases * 10 + spending / 100, 2)

purchases = int(input("Purchases: "))
spending = float(input("Total spending: "))

print("Customer score:", customer_score(purchases, spending))
