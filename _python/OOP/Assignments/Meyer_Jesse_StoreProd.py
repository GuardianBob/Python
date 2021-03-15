uid = 10

class Store:
    def __init__(self, s_name):
        self.name = s_name
        self.products = []

    def add_product(self, new_product): # takes a product and adds it to the store
        self.products.append(new_product)
        return self

    def sell_product(self, id): # remove the product from the store's list of products given the id 
        # (assume id is the index of the product in the list) and print its info.
        pSold = self.products[id]       
        self.products.remove(pSold)
        pSold.print_info()
        return self

    def sell_productUid(self, uid): # remove the product from the store's list of products given the Unique ID
        # (assume id is the index of the product in the list) and print its info.
        for p in self.products:
            if p.id == uid:
                pSold = p   #self.products.id[uid]   
                self.products.remove(pSold)
                print("Sold: ")
                pSold.print_info()
                return self

    def inflation(self, percent_increase): # increases the price of each product by the percent_increase given 
        # (use the method you wrote in the Product class!)
        for i in self.products:
            Product.update_price(i, percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount): # updates all the products matching the given category by 
        # reducing the price by the percent_discount given (use the method you wrote in the Product class!)
        for i in self.products:
            if i.category == category:
                Product.update_price(i, percent_discount, False)
        return self
    
    # Needed a way to list all store items without havinf to iterate through the list each time I tried to print it
    def list_inventory(self, cat=""):
        print("\n","="*80, f"\nCurrent {self.name} {cat} Inventory:\n")        
        for i in self.products:
            if cat != "":
                if i.category == cat:
                    i.print_info()
            else:
                i.print_info()
        print("="*80, "\n")

class Product:
    def __init__(self, pName, pPrice, pCategory):        
        self.id = uid
        auto_inc()
        self.name = pName
        self.price = pPrice
        self.category = pCategory     
                
    def update_price(self, percent_change, is_increased): # updates the product's price. 
        # If is_increased is True, the price should increase by the percent_change provided. 
        # If False, the price should decrease by the percent_change provided.
        if is_increased == True:
            self.price = self.price * (1+percent_change)
        elif is_increased == False:
            self.price = self.price * (1-percent_change)
        return self

    def print_info(self):  # print the name of the product, its category, and its price.
        print(f"{self.name}:  Category: {self.category}, Price: ${'%.2f'%self.price}")
        return self

# BONUS  -  Unique ID Generator
def auto_inc():
    global uid
    uid += 1
    return uid

# Create store and Products
gStore = Store("Vons")
bananas = Product("Bananas", 1.10, "Fruit")
apples = Product("Apples", 1.30, "Fruit")
carrots = Product("Carrots", 1.50, "Vegetable")
peppers = Product("Peppers", 1.20, "Vegetable")

# Check UID counter
print(carrots.id)

# #Print product Info
# peppers.print_info()

#Add Products to Store
gStore.add_product(bananas).add_product(apples).add_product(carrots).add_product(peppers)
# #List Store Inventory
# gStore.list_inventory()

# #List Store Inventory by Category
# gStore.list_inventory("Fruit")

# #Sell Product by id and print info
# gStore.sell_product(2)
# gStore.list_inventory()

#Sell Product by Unique ID and print info
gStore.sell_productUid(carrots.id)
gStore.list_inventory()

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

