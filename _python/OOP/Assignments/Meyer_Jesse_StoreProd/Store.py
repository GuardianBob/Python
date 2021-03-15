from Product import Product

class Store:
    def __init__(self, s_name):
        self.name = s_name
        self.products = []

    def new_Store(self, s_name):
        self.name = s_name
        self.products = []

    def add_product(self, new_product): # takes a product and adds it to the store
        self.products.append(new_product)
        return self

    def sell_product(self, id): # remove the product from the store's list of products given the id 
        # (assume id is the index of the product in the list) and print its info.
        pSold = self.products[id]       
        self.products.remove(pSold)
        print("Sold: ")
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