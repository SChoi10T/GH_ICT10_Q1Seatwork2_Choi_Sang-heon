# Data Types in Python
from pyscript import display

# Variables
restaurant_name = "Sweet Choi's"  # String
owner_name = "Sang-heon G. Choi"  # String
year_established = 2021  # Integer
popular_item_price = 349.9  #Float
has_delivery = True  # Boolean
product_names = ["Fondant Cake", "Sweet Cupcakes", "Chocolate Cookies", "Vanila Sundae", "Flavored Bread", "Choi's Special"]  # List
business_hours = "Open: 12:00 PM - 9:00 PM" # String
menu_prices = (70.0, 60.0, 75.0, 80.0, 456.0) # Tuple
common_allergens = "Nuts, Milk, Eggs, Soy, and Wheat" # String
tax_rate = 7.5 # Float

# Header Section
display(f"{restaurant_name}", target = "restaurant_name")
display(f"Owner: {owner_name}", target = "owner_name")
display(f"Since {year_established}", target = "year_established")

# Menu
display(f"Tax Rate: {tax_rate}%", target = "tax_rate")

display(f"{product_names[0]}: Popular Choice!", target = "Fondant_Cake")
display(f"{popular_item_price} ₱", target = "popular_item_price")

display(f"{product_names[1]}", target = "Sweet_Cupcakes")
display(f"{menu_prices[0]} ₱", target = "menu_price1")

display(f"{product_names[2]}", target = "Chocolate_Cookies")
display(f"{menu_prices[1]} ₱", target = "menu_price2")

display(f"{product_names[3]}", target = "Vanila_Sundae")
display(f"{menu_prices[2]} ₱", target = "menu_price3")

display(f"{product_names[4]}", target = "Flavored_Bread")
display(f"{menu_prices[3]} ₱", target = "menu_price4")

display(f"{product_names[5]}", target = "Chois_Special")
display(f"{menu_prices[4]} ₱", target = "menu_price5")

# Delivery and Business Hours
display(f"Caution: Some products may contain common allergens such as {(common_allergens)}", target="common_allergens")

if has_delivery:
    display("Delivery service is available! Order now!", target="deliveryservice")
else:
    display("Sorry, delivery service is unavailable!", target="deliveryservice")

display(f"{business_hours}", target = "business_hours")