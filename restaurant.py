## Importing marketing module

import marketing as mkt

## importing order module

import order as ord

## Creating a restaurant class

class Restaurant():

    def __init__(self,rest_name, food_type,loc):
        self.rest_name = rest_name
        self.food_type = food_type
        self.loc = loc

the_lobster = Restaurant("The Lobster", "seafood", "Metro Manila")
the_chicken = Restaurant("The Chicken", "fried chicken place", "Metro Manila")
the_farm = Restaurant("The Farm", "vegetarian options", "Quezon City")

## Append the restaurant in a list

restaurants = [the_lobster,the_chicken,the_farm]

for rest in restaurants:
    print("\n## ------ ##")
    print(f"RESTAURANT NAME: {rest.rest_name}")
    print(f'FOOD TYPE: {rest.food_type}')
    print(f'LOCATION: {rest.loc}')

print("\n------------------------------------------------------->")

for rest in restaurants:
    mkt.describe_restaurant(rest)

mkt.end_marketing()

print("\n------------------------------------------------------->")


angela = ord.Customer("Angela","Metro Manila","seafood")
robert = ord.Customer("Robert","Metro Manila","vegetarian options")

ord.match_restaurant(angela,the_lobster)