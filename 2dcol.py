# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["calery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# fruits[0] = 
# print(fruits)

groceries = ["apple", "orange", "banana", "coconut"], ["calery", "carrots", "potatoes"],["chicken", "fish", "turkey"]

for collection in groceries:
  for food in collection:
    print(food, end =" ")
  print()
