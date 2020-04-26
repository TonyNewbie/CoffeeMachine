pizzas = 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy'
salads = 'Caesar salad, Green salad, Tuna salad, Fruit salad'
soups = 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'
order = input()
if order == 'pizza':
    print(pizzas)
elif order == 'salad':
    print(salads)
elif order == 'soup':
    print(soups)
else:
    print("Sorry, we don't have it in the menu")
