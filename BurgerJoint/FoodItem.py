class FoodItem:
  price=0
  name=""
  def __init__(self,name,price):
    self.name=name
    self.price=price
  def display(self):
    print(self.__dict__)
