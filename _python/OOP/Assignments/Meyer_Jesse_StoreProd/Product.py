
class Product:
    def __init__(self, pName, pPrice, pCategory):        
        self.id = uid
        auto_inc()
        self.name = pName
        self.price = pPrice
        self.category = pCategory 

    def  new_Item(self, pName, pPrice, pCategory):        
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

uid = 0

# BONUS  -  Unique ID Generator
def auto_inc():
    global uid
    uid += 1
    return uid