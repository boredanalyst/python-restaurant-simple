def announce(rest):
    print("\n## ------- ##")
    print(f'Go to this restaurant, {rest.rest_name}, now!')

def end_marketing():
    print("\n## -------- ##\n")
    print("That's it for the announcements today!")

def describe_restaurant(rest):
    print("\n## -------- ##\n")
    print(f'This restaurant, {rest.rest_name}, is a restaurant that specializes in {rest.food_type}.')
    print(f'This wonderful restaurant is located in {rest.loc}.')
    