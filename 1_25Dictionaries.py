# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates 

capitals = {"USA": "Whashington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
#if capitals.get("Russia"):
#    print("That capital exists")
#else:
#    print("Taht capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
   #print(key)

#print(keys)
#values = capitals.values()
#print(values)
#for value in capitals.values():
 # pint(value)
#items = capitals.items() 
#print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
