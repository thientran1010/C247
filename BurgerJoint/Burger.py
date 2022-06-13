import FoodItem

class Burger(FoodItem):
    
    patty=""
    # add lettuce, pickles, tomatoes, and sauce
    extras=[]
    def __init__(self, name, price, patty):
        FoodItem.__init__(self, name, price)
        self.patty=patty
        self.extras

    def display(self):
        print(self)    