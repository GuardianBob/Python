class Cup:
    def __init__(self, materialOfCup, colorOfCup):
        #ATTRIBUTES GO HERE (inside the __init__ function)
        self.material = materialOfCup
        self.color = colorOfCup
        self.percent_filled = 0
        
    # METHODS
    def fill(self, amountOfLiquid):
        self.percent_filled += amountOfLiquid
        return self

    def pout(self, amountOfLiquid):
        self.percent_filled -= amountOfLiquid
        return self

    def spill(self):
        self.percent_filled = self.percent_filled / 2
        return self

    def say_info(self):
        print(f"this {self.color} {self.material} cup is {self.percent_filled}% full.")
        return self

# Instances are made outside the class
paperCup = Cup("paper", "white")
myFavoriteCup = Cup("plastic", "blue")
glassCup = Cup("glass", "clear")


myFavoriteCup.fill(60)
myFavoriteCup.spill()
myFavoriteCup.pour(13)
myFavoriteCup.say_info()
