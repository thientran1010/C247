import FoodItem

class Burger(FoodItem):
    
    patty=""
    type=""
    def __init__(self, name, price, patty, type):
        FoodItem.__init__(self, name, price)
        self.patty=patty
        self.type=type

    def display(self):
        print(self)    