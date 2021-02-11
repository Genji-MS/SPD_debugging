# by Kami Bigdely
# Consolidate conditional expressions
def dice(ingredients):
    print("diced all ingredients.")

def mix_all(diced_ingredients):
    print("mixed all.")

def add_salt():
    print('added salt.')

def pour(liquid):
    print('poured', liquid + '.',)

def make_shirazi_salad(ingredients):
    cucumber = 'cucumber' not in ingredients
    tomato = 'tomato' not in ingredients
    onion = 'onion' not in ingredients
    lemon = 'lemon juice' not in ingredients
    if cucumber or tomato or onion or lemon:
        print('lacks ingredients.')
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])