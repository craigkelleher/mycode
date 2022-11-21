#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]

for x in NE_animals:
    print(f"all the animals from the NE farm are: {x}")


# Part 2:
# print menu to choose from
for farm in farms:
    print(farm["name"])

# take user input
answer=input("Choose a farm: NE Farm, W Farm, SE Farm, to return the plants/animals that are raised on that farm\n")

# compare user input and print matches
for farm in farms:
    if farm["name"].lower() == answer.lower():
        # x = farm["agriculture"]
        # print(x)
        for critter in farm["agriculture"]:
            print(critter)
        break

# part 3:
# return a farm but only get the animals
yuck= ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        for ag_item in farm["agriculture"]:
            if ag_item not in yuck:
                 print(ag_item)

