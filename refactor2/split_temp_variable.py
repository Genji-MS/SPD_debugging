# by Kami Bigdely
# Split temporary variable

PATTY = 70 # [gr]
PICKLE = 20 # [gr]
TOMATOES = 25 # [gr]
LETTUCE = 15 # [gr]
BUNS = 95 # [gr]
KIMCHI = 30 # [gr]
MAYO = 5 # [gr]
FRIED_ONION = 20 # [gr]
Burger_NY = {
    PATTY : 2,
    PICKLE : 4,
    TOMATOES : 3,
    LETTUCE : 2,
    BUNS : 2,
    KIMCHI : 0,
    MAYO : 0,
    FRIED_ONION : 0
}
Burger_Seoul_Kimchi = {
    PATTY : 2,
    PICKLE : 4,
    TOMATOES : 3,
    LETTUCE : 0,
    BUNS : 2,
    KIMCHI : 1,
    MAYO : 1,
    FRIED_ONION : 1
}

sandwich_weight = calc_sandwich_weight("Burger_NY")
print("NY Burger Weight", sandwich_weight)
sandwich_weight = calc_sandwich_weight("Seoul_Kimchi")
print("Seoul Kimchi Burger Weight", sandwich_weight)

def calc_sandwich_weight(burger_name):
    """Allows user to use specified regular menu item by name"""
    predefined_burgers = {
        "NY": Burger_NY,
        "Seoul_Kimchi": Burger_Seoul_Kimchi        
    }
    s = predefined_burgers[burger_name]
    return calc_sandwich_weight(s[PATTY], s[PICKLE], s[TOMATOES], s[LETTUCE], 
                                s[BUNS], s[KIMCHI], s[MAYO], s[FRIED_ONION])

def calc_sandwich_weight(patty, pickle, tomatoes, lettuce, buns, kimchi, mayo, onion)
    """Calculates weight by individual components"""
    total = 0
    quantity = [patty, pickle, tomatoes, lettuce, buns, kimchi, mayo, onion]
    weight = [PATTY, PICKLE, TOMATOES, LETTUCE, BUNS, KIMCHI, MAYO, FRIED_ONION]

    for i in range(0,len(quantity)-1):
        total += weight[i] * quantity[i]
    return total