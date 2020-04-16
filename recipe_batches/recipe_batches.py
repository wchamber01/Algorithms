#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # Implement counter & temp arr to store values
    batch_counter = 0
    temp_arr = []
    
    if recipe.keys() == ingredients.keys():
        
        # Get all ingredients
        for i in ingredients:
            if ingredients[i] >= recipe[i]:
                
                # Compare & divide values
                x = ingredients[i] // recipe[i]
                # Add values to temp_arr
                temp_arr.append(x)
                # Find min value in temp_arr and assign value to counter
                batch_counter = min(temp_arr)
                return batch_counter
                print ("You have enough ingredients to make",{batch_counter},"batch(es).")
    else:
        # Handle cases where recipe calls for nonexistent item(s) by returning 0
        print("You don't have all the ingredients.")
        return 0

if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))