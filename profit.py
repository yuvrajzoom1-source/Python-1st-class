actual_price = float(input("enter actual cost?"))
sale_price = float(input("enter sale price?"))
if sale_price>actual_price:
    profit= sale_price-actual_price
    print(f"total profit amount is {profit}")