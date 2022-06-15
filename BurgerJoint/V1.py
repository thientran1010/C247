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
    'salad':5.45,
    "burger": {
            "beef": 6.0,
            "chicken": 5.0,
            "veggie": 6.0,
            "single": 0.0,
            "double": 1.0
        }
}



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
  toppings=[] 
  is_name=False 
  is_patty=False  
  topping_counter=0

  while is_name == False:
    name = input("Select a burger: ")
    name = name.lower()
    if name in menu["burger"]:
      break
    else: 
      print("Not an option. Please select again.")
  while is_patty == False:
    patty = input("Do you want a single or double patty: ")
    patty = patty.lower()
    if patty == "double" or patty == "single": 
      break
    else: 
      print("Not an option. Please try again.")
  want_more=True
  good_input=False
  
  while topping_counter < 4 and want_more==True:
        topping = input("What toppings do you want? Onions, lettuce, tomatoes, and/or pickles. Say all if you want all of these toppings: ")
        topping = topping.lower()
        if topping == 'all':
            toppings = ["onions", 'lettuce', 'tomatoes', 'pickles']
            break  
        elif (topping ==  "onions" or topping == 'lettuce' or topping == 'tomatoes' or topping == 'pickles') and toppings.count(topping) == 0:
            print(topping)
            toppings.append(topping)
            topping_counter += 1
            while good_input == False:
              ask_for_more = input("Do you want more toppings? (y/n): ")
              if ask_for_more.lower() == "y" or ask_for_more.lower() == "yes":
                break
              elif ask_for_more.lower() == "n" or ask_for_more.lower() == "no":
                want_more=False
                break
              else: 
                print("Please enter the correct response.")
        elif toppings.count(topping) > 0:
          print("Please add another one you already have this topping")    
        else:
            print("I don't understand please try again.")
         
  b = Burger(name, menu["burger"][name], patty, toppings)

  if b.patty.lower() == "double":
        b.price += 1
  print(b.price)
  finalized=bool(input("Do you finish ordering burger? True/False "))
  if finalized:
    return b
  return False

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

  
  

