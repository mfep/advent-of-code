import re

foods = []
with open('day21.txt') as f:
  for line in f:
    parens_open = line.find('(')
    ingredients = set(line[:parens_open].split())
    allergens = set(line[parens_open + len('(contains ') : -2].split(', '))
    foods.append((ingredients, allergens))

solutions = {}
for ingredients, allergens in foods:
  for allergen in allergens:
    if allergen not in solutions:
      solutions[allergen] = set(ingredients)
    else:
      solutions[allergen] = solutions[allergen].intersection(ingredients)

not_allergen_ingredients = set()
for ingredients,_ in foods:
  for ingredient in ingredients:
    not_allergen_ingredients.add(ingredient)

for possible_ingredients in solutions.values():
  not_allergen_ingredients = not_allergen_ingredients.difference(possible_ingredients)

occurences = 0
for ingredients,_ in foods:
  for ingredient in ingredients:
    if ingredient in not_allergen_ingredients:
      occurences += 1

print(occurences)
