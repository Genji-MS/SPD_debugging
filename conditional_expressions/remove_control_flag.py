# by Kami Bigdely
# Remove control flag
def find_food(food, fridge):
    if food in fridge:
        return True
    return False

if __name__ == "__main__":
    food = 'wesabi'
    food_list = ['onion', 'cucumber', 'Guacamole', 'kabob barg', 'wesabi']
    found_item = find_food(food, food_list)
    print(food, "Found: " + found_item)