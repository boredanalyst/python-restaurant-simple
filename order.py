## This is a module for odering good sand items

class Customer():
    def __init__(self,cust_name,cust_loc,cust_pref):
        self.name = cust_name
        self.loc = cust_loc
        self.pref = cust_pref
    
def order_item(cust):
    print(f'Welcome {cust.name}! What is your order today?')

def match_restaurant(cust,rest):
    print("## ----- ##")
    print(f"Let's see if {cust.name} and {rest.food_type} are a match!")
    print(f"CUSTOMER PREFERENCE: {cust.pref.upper()}")
    print(f"RESTAURANT FOOD TYPE: {rest.food_type.upper()}")

    if cust.pref == rest.food_type:
        print("This customer and the restaurant are a match!")
    else:
        print("This customer and the restaurant are NOT a match")