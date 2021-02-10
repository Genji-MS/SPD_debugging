# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
self.discount_factor

def get_price(quantity, item_price):
    base_price = quantity * item_price
    calc_discount(base_price)
    return base_price * self.discount_factor

def calc_discount(base_price):
    if base_price > 1000: 
        self.discount_factor = 0.95
    else: 
        self.discount_factor = 0.98