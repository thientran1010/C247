import FoodItem

class Burger(FoodItem):
    
    def __init__(self, name, price):
        FoodItem.__init__(self, name, price)

    def display(self):
        print(self)    