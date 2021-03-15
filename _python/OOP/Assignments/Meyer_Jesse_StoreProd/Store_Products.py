from Store import Store
from Product import Product

# Create store and Products
gStore = Store("Vons")
bananas = Product("Bananas", 1.10, "Fruit")
apples = Product("Apples", 1.30, "Fruit")
carrots = Product("Carrots", 1.50, "Vegetable")
peppers = Product("Peppers", 1.20, "Vegetable")

# # Check UID counter
# print(carrots.id)

# #Print product Info
# peppers.print_info()

#Add Products to Store
gStore.add_product(bananas).add_product(apples).add_product(carrots).add_product(peppers)
# #List Store Inventory
# gStore.list_inventory()

# #List Store Inventory by Category
# gStore.list_inventory("Fruit")

# #Sell Product and print info
# gStore.sell_product(2)
# gStore.list_inventory()

#  ===============SENSEI BONUS=======================
# #Sell Product by Unique ID and print info
# gStore.sell_productUid(carrots.id)
# gStore.list_inventory()

# # Increase Price
# bananas.print_info()
# bananas.update_price(.1, True)
# bananas.print_info()

# # Decrease Price
# apples.print_info()
# apples.update_price(.1, False)
# apples.print_info()

# # Inflation
# gStore.list_inventory()
# gStore.inflation(.2)
# gStore.list_inventory()

# # Clearance
# gStore.list_inventory()
# gStore.set_clearance("Fruit", .5)
# gStore.list_inventory()