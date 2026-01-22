import math

def pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 2) / 100  # convert cm to meters
    area = math.pi * radius_m ** 2
    return price_usd / area


def compare_pizzas():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))

    unit_price1 = pizza_unit_price(d1, p1)
    unit_price2 = pizza_unit_price(d2, p2)

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")
compare_pizzas()