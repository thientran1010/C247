menu = { "burger": 5.00 }


d={
    "name": "Burger",
   "price": 0
}


class FoodItem:
  price=0
  name=""
  def __init__(self,name,price):
    self.name=name
    self.price=price
  def display(self):
    print(self.__dict__)


class Drink(FoodItem):
    #size is 1 for small, 2 for medium, 3 for large
    size=0
    #with ice or not
    ice=0
    def __init__(self,name,price,size,ice):
        FoodItem.__init__(self,name,price)
        self.size=size
        self.ice=ice
    def display(self):
        print(self.__dict__)

class Side(FoodItem):
  size=""
  def __init__(self,name,price,size):
    FoodItem.__init__(self,name,price)
    if size in ('small','medium','large'):
      self.size=size
    else: print("error")
  def display(self):
    print(self.__dict__)
  def changeSize(self,size):
    self.size=size

class Burger(FoodItem):
    
    patty=""
    
    def __init__(self, name, price, patty):
        FoodItem.__init__(self, name, price)
        self.patty=patty

    def display(self):
        print(self)    

class Order:
  # menu ={
  #   "soda":1.00,
  #   'salad':5.45,
  #   'meat burger': 8.35
  # }
  cost = 0
  items=[]
  def __init__(self):
    self.cost=0
    self.items=[]
  def add(self,item):
    self.items.append(item)

  def calculateTotal(self):
    self.cost = sum([i.price for i in self.items])

  def display(self):
    for i in self.items:
      i.display()
    print("Total cost is ${}".format(self.cost))


ordering=True
#while(True):
menu ={
    "soda":1.00,
    'salad':5.45
}

def createBurger():
  name = input("Select a burger: ")
  pass

def createDrink():
  name = input("Select a drink: ")
  size = input("Select the size of the drink: ")
  ice = input("Do you want it with ice: ")
  drink = Drink(name,menu[name],size,ice)
  finalized=bool(input("Do you finish ordering side? True/False "))
  if finalized:
    return drink
  return False

def createSide():
  name = input("Select a side: ")
  size = input("Select the size of the side: ")
  s = Side(name,menu[name],size)
  finalized=True
  finalized=bool(input("Do you finish ordering side? True/False "))
  if finalized:
    return s

def createBurger():
  name = input("Select a side: ")
  size = input("Select the size of the burger: ")
  patty = input("Select the patty of the burger (single/double): ")
  s = Side(name,menu[name],patty)
  finalized=True
  finalized=bool(input("Do you finish ordering side? True/False "))
  if finalized:
    return s
  pass

def userInput():
  order=Order()
  cont= input("Do you want to order (True/False): ")
  while(cont=='True'):
    orderType = input("Please choose type of order (combo, burger, drink, side): ")
    if orderType.lower() == 'drink':
      drink = createDrink()
      if drink is not None: order.add(drink)
    if orderType.lower() == 'side':
      s = createSide()
      if s is not None: order.add(s)
    cont= input("Do you want to order (True/False): ")
  
  order.calculateTotal()
  order.display()

  
  

