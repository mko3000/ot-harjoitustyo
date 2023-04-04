class Recipe:
    '''Recipe entity class'''
    def __init__(self, name, ingredients, steps, description, score):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.description = description
        self.tags = []
        self.times_made = 0
        self.reviews = []

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_review(self, review):
        self.reviews.append(review)

    def add_times_made(self):
        self.times_made += 1

    def __str__(self) -> str:
        return f'{self.name}, {self.ingredients}, {self.steps}, {self.description}, {self.tags}, {self.times_made}, {self.reviews}'


class Ingredient_list:
    '''Ingredient list entity class'''
    def __init__(self):
        self.ingredients = {}

class Ingredient:
    '''Ingredient entity class'''
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit
        self.tags = []
        self.allergens = []

    