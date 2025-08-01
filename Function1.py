# function that takes a price and tax rate and return total price
def calculate_total_price(price, tax_rate):
    tax_amount = price * tax_rate
    total_price = price + tax_amount
    return total_price


# Let's use the function
item_price = 100
sales_tax = 0.05

final_price = calculate_total_price(item_price, sales_tax)
print(f"Total amount for the first item  {final_price}")

another_item_price = 80
second_item = calculate_total_price(another_item_price, 0.08)
print(f"Total amount for second item: {second_item}")
