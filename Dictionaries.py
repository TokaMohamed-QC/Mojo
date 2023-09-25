#Dictionaries

stuff = {"Food": 15, "energy": 100, "enemies": 3}

print(stuff.get("Food"))

print(stuff.items())

print(stuff.keys())

print (stuff.popitem())

print (stuff)

print (stuff.setdefault("Food"))

print (stuff)

print (stuff.setdefault("Friends", 123))

print (stuff)

new_stuff = {"Electricity": 150, "Greetings": 50}

stuff.update(new_stuff)

print (stuff)

stuff.update(Food = 50, cookies = 100)

print(stuff)