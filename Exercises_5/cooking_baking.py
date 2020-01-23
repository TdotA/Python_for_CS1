##########################################################################
# Cooking and baking 
#
# Ingredients that are needed to prepare a dish can be given by a dictionary,
# where keys are ingredients and values are amounts of the corresponding
# ingredients that are needed to prepare the dish.
##########################################################################



##########################################################################
# Write a function scale_recipe(recipe, factor) that creates and returns
# a new recipe. It should contain the same ingredients as `recipe`, with
# the difference that all amounts are scaled by the factor `factor`.
# Example:
# 
#     >>> scale_recipe({'eggs': 4, 'flour': 500}, 2)
#     {'eggs': 8, 'flour': 1000}
##########################################################################

def scale_recipe(recipe, factor):
    for i in recipe: 
        recipe[i] = recipe[i] * factor
    return recipe 
#print(scale_recipe({'eggs': 4, 'flour': 500}, 2))
         
##########################################################################
# Write a function have_ingredients(recipe, pantry) that checks if there
# is sufficient amount of ingredients in the pantry for the given recipe.
# Ingredients in the pantry are given by the dictionary `pantry`. Ingredients
# that are needed for the recipe are given by the dictionary `recipe`.
# Example:
# 
#     >>> have_ingredients({'eggs': 3, 'flour': 500}, {'flour': 600})
#     False
##########################################################################

def have_ingredients(recipe, pantry):
    for i in recipe:
        if not(i in pantry):
            return False
            break
        elif (recipe[i] >= pantry[i]):
            return False
            break
    return True 
#print(have_ingredients({'eggs': 3, 'flour': 500}, {'flour': 600, 'eggs' : 2}))

##########################################################################
# Write a function purchase(recipe, pantry) that returns a dictionary
# which contains ingredients and the amounts that we need to purchase
# in order to prepare the dish. Example:
# 
#     >>> purchase({'eggs': 3, 'flour': 500}, {'flour': 1000, 'sugar': 1000})
#     {'eggs': 3}
##########################################################################

def purchase(recipe, pantry):
    cart={}
    for i in recipe:
        if not(i in pantry):
            cart[i] = recipe[i]
        elif (recipe[i] > pantry [i]):
            cart[i] = recipe[i] - pantry[i]
        else:
            continue
    return cart 
print(purchase({'eggs': 3, 'flour': 500}, {'flour': 400, 'sugar': 1000}))

