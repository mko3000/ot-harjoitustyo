
import json

from entities.recipe import Recipe


def add_recipe():
    '''Add a recipe to the recipe manager'''
    name = input('Enter recipe name: ')
    ingredients = input('Enter ingredients: ')
    steps = input('Enter steps: ')
    description = input('Enter description: ')
    score = input('Enter score: ')
    recipe = Recipe(name, ingredients, steps, description, score)
    #recipe_manager.add_recipe(recipe)
    print(recipe)
    print()

add_recipe()