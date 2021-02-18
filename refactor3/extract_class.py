# by Kami Bigdely
# Extract Class
foods = {'butternut squash soup':[45, True, 'soup','North African',\
     ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
        ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
          'they get soft and golden on top 2. Put all in blender with'
          'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
               '. Add coconut milk. Simmer for 5 mintues.'],
        'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
            '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                '4. Mixed them thoroughly'],
        'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
            'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                'the seasonings 2. In a bowl, mix ground beef with the'
                'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

for key, value in foods.items():
    # this appears to run just fine as it is. I don't see any way to reformat this other then cha
    TIME = 0
    VEGGIE = 1
    TYPE = 2
    CUISINE = 3
    INGREDIENTS = 4
    RECIPE = 5
    print("Name:",key)
    print("Prep time:",value[TIME], "mins")
    print("Is Veggie?", 'Yes' if value[VEGGIE] else "No")
    print("Food Type:", value[TYPE])
    print("Cuisine:", value[CUISINE])
    print("Ingredients:")
    for ingredient in value[INGREDIENTS]:
        print(ingriedient, end=', ')
    print()
    print("recipe", value[RECIPE])
    print("***")