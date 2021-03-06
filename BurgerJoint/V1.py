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
    # add lettuce, pickles, tomatoes, and sauce
    toppings=[]
    def __init__(self, name, price, patty, toppings):
        FoodItem.__init__(self, name, price)
        self.patty=patty
        self.toppings=toppings

    def display(self):
        print(self.__dict__)    

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
menu ={
    'soda':{
        'small':1.0,
        'medium':1.20,
        'large':1.30
    },
    'coffee':{
        'small':3.00,
        'medium':4.00,
        'large':5.00
    },
    'juice':{
        'small':2.00,
        'medium':3.00,
        'large':4.00
    },

    'salad':5.45,
    "burger": {
            "beef": 6.0,
            "chicken": 5.0,
            "veggie": 6.0,
            "single": 0.0,
            "double": 1.0
        }
}

side_menu={
    "salad":5.85,
    "poutine":6.30,
    "wrap":5.75
}
size_side_menu={
    "small":0,
    "medium":1.00,
    "large":2.00
}
d={'soda1':1.00,
'soda2':1.20,
'soda3':1.30,

'coffee1':3.00,
'coffee2':4.00,
'coffee3':5.00,

'juice1':2.00,
'juice2':3.00,
'juice3':4.00,
}

def createDrink():
    
  name_counter=0
  while name_counter < 1:
        name = input("What type do you want? coffee or juice or soda")
        name=name.lower()
        if  name ==  'coffee' or name == 'juice' or name == 'soda':
            name_counter += 1
        else:
            print("I don't understand please try again.")

  drink_counter=0
  while drink_counter < 1:
        size = input("What size do you want? small or medium or large")
        size = size.lower()
        if  size ==  'small' or size == 'medium' or size == 'large':
            drink_counter += 1
        else:
            print("I don't understand please try again.")
            
  ice_counter=0
  while ice_counter < 1:
        ice = input("Do you want it with ice: true or false")
        ice = ice.lower()
        if  ice ==  'true' or ice == 'false':
            ice_counter += 1
        else:
            print("I don't understand please try again.")


  drink = Drink(name,menu[name][size],size,ice)
  finalized=bool(input("Do you finish ordering drink? True/False "))
  if finalized:
    return drink
  return False



def createSide():
  print(side_menu.keys())
  name = input("Select a side: ")
  while name.lower() not in side_menu.keys():
    print("Item not on the list. Try again")
    name = input("Select a side: ")
  print(size_side_menu.keys())
  size = input("Select the size of the side: ")
  while size.lower() not in size_side_menu.keys():
    print("Item not on the list. Try again")
    size = input("Select a side: ")
  s = Side(name,side_menu[name]+size_side_menu[size],size)
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
  want_topping=True
  while want_topping == True:
      does_user_want = input("Do you want to add toppings? y/n: ")
      if does_user_want.lower() == "y" or does_user_want.lower() == "yes":
          while topping_counter < 4 and want_more==True:
            topping = input("What toppings do you want? Onions, lettuce, tomatoes, and/or pickles. Say all if you want all of these toppings: ")
            topping = topping.lower()
            if topping == 'all':
                toppings = ["onions", 'lettuce', 'tomatoes', 'pickles']
                break  
            elif (topping ==  "onions" or topping == 'lettuce' or topping == 'tomatoes' or topping == 'pickles') and toppings.count(topping) == 0:
                toppings.append(topping)
                topping_counter += 1
                while good_input == False:
                  ask_for_more = input("Do you want more toppings? (y/n): ")
                  if ask_for_more.lower() == "y" or ask_for_more.lower() == "yes":
                    break
                  elif ask_for_more.lower() == "n" or ask_for_more.lower() == "no":
                    want_more=False
                    want_topping=False
                    break
                  else: 
                    print("Please enter the correct response.")
            elif toppings.count(topping) > 0:
              print("Please add another one you already have this topping")    
            else:
                print("I don't understand please try again.")
      elif does_user_want.lower() == "n" or does_user_want.lower() == "no":
            break
      else:
                print("Please enter the correct response.")
         
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
  while(cont.lower() =='true'):
    orderType = input("Please choose type of order (combo, burger, drink, side): ")
    if orderType.lower() == 'drink':
      drink = createDrink()
      if drink is not None: order.add(drink)
    if orderType.lower() == 'side':
      s = createSide()
      if s is not None: order.add(s)
    if orderType.lower() == 'burger':
      s = createBurger()
      if s is not None: order.add(s)
    cont= input("Do you want to continue to order (True/False): ")
  
  order.calculateTotal()
  order.display()
