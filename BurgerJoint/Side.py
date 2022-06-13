class Side(FoodItem):
  size=""
  def __init__(self,name,price,size):
    FoodItem.__init__(self,name,price)
    if size in ('small','medium','large'):
      self.size=size
    else: print("error")
  def display(self):
    print(self.__dict__)
