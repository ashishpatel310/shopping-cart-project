products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...
#print(products)

# an infinite loop! you can press control+c to cancel the program if/when it gets stuck...

selected_ids = []


while True:
    x = input("Please scan an item, or 'Select done' if there are no more items: ")
    selected_ids.append(x)
    print(x)
    if x == "done":
        break

print(selected_ids)

del selected_ids[-1]

print("-----------------------------------------")
print("Ashish's Grocery Store")
print("-----------------------------------------")
print("Web: www.AshishGotTheGoods.com")
print("Phone: 1.240.780.1455")
import datetime
now = datetime.datetime.now()
print("Checkout Time: " + str(now))
print("-----------------------------------------")


running_total = 0


for s in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == s]
    matching_p = matching_products[0]
    price_usd = "${0:.2f}".format(matching_p["price"])
    print(" + " + matching_p["name"] + " (" + str(price_usd) + ")")
    running_total = running_total + matching_p["price"]


total_tax = running_total * .18
total = total_tax + running_total



print("----------------------------------------")
print("Pre-Tax Total: " + str(running_total))
print("Sales Tax: " + str(total_tax))
print("Total: " + str(total))

print("----------------------------------------")
print("Thanks! Come again soon!")



#a = [int(x) for x in input().split()]
#print(a)
#item_count = len(a)
#print(len(a))
#
#x = 0
#
#running_total = 0
#
#while x < item_count:
#    selected_id = 1 #input("Please Scan an Item")
#    matching_products = [p for p in products if p["id"] == selected_id]
#    product = matching_products[0]
#    price = product["price"]  
#    running_total = running_total + price
#    x = x + 1
#
#print("THE TOTAL PRICE IS: " + str(running_total))
#
#
#

