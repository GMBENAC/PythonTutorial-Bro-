
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# groceries = [["apple", "orange", "banana", "coconut"],["celery", "carrots", "potatoes"],["chicken", "fish", "turkey"]]

# print(groceries[1])
# print(groceries[0][1])
# print(groceries)

# for collection in groceries:
    #print(collection)

# for collection in groceries:
    # for food in collection:
        # print(food, end=" ")

# Example 1

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()