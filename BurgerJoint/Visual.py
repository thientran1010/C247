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


# user interface 
# work on error detection
# presentation:

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
c={
  "small":"1",
    "medium":"2",
    "large":"3"
}

import PySimpleGUI as sg
welcome=[
    [sg.Text("Do you want to order")],
    [sg.Button("OK")],
    [sg.Button("Cancel")]
]
orderType=[
    [sg.Button("View order")],
    [sg.Text("Please choose an order type")],
    [sg.Button("combo")],
    [sg.Button("burger")],
    [sg.Button("drink")],
    [sg.Button("side")],
    [sg.Text("Payment")],    
    [sg.Button("Credit")]
    
]
drinkType=[
    [sg.Text("Please choose your beverage")],
    [sg.Button("soda")],
    [sg.Button("coffee")],
    [sg.Button("juice")],
    
]
drinkSize=[
    [sg.Text("Please choose your size")],
    [sg.Button("small")],
    [sg.Button("medium")],
    [sg.Button("large")],
    
]
drinkIce=[
    [sg.Text("Do you want it with ice?")],
    [sg.Button("Yes")],
    [sg.Button("No")],
    
]

window=sg.Window(title="Welcome",layout=welcome,margins=(100,50))

orderTypeWindow=sg.Window(title="OrderType",layout=orderType,margins=(100,50))
drinkTypeWindow=sg.Window(title="DrinkType",layout=drinkType,margins=(100,50))
drinkSizeWindow=sg.Window(title="DrinkSize",layout=drinkSize,margins=(100,50))
drinkIceWindow=sg.Window(title="drinkIce",layout=drinkIce,margins=(100,50))


order=Order()

event,values = window.read(close=True)

if event == "OK":
    event,values=orderTypeWindow.read(close=True)
if event == "View order":
    sg.popup("None")
    event,values = window.read(close=True)

def user_input_drink():
    drinkType=[
    [sg.Text("Please choose your beverage")],
    [sg.Button("soda")],
    [sg.Button("coffee")],
    [sg.Button("juice")]
    
    ]
    drinkSize=[
        [sg.Text("Please choose your size")],
        [sg.Button("small")],
        [sg.Button("medium")],
        [sg.Button("large")],

    ]
    drinkIce=[
        [sg.Text("Do you want it with ice?")],
        [sg.Button("Yes")],
        [sg.Button("No")],

    ]

    n,values=drinkTypeWindow.read(close=True)
    s,values=drinkSizeWindow.read(close=True)
    i,values=drinkIceWindow.read(close=True)
    drink=Drink(n,d[n+c[s]],s,i)
    drinkConfirm=[
    [sg.Text("Beverage {} Size {} with ice {} price $ {} to your order".format(n,s,i,d[n+c[s]]))],
    [sg.Text("Do you want it to the order?")],
    [sg.Button("Yes")],
    [sg.Button("No")],
    
    ]
    
    drinkConfirmWindow=sg.Window(title="drinkConfirm",layout=drinkConfirm,margins=(100,50))
    event,values = drinkConfirmWindow.read(close=True)
    if event == 'Yes':
        sg.popup("Items added to your order. Return to the main menu")
        return Drink(n,d[n+c[s]],s,i)
    else:
        sg.popup("Items discarded. Return to the main menu")
        return None
    

if event == "drink":
    a = user_input_drink()
    if (a != None):
        order.add(a)

event,values=orderTypeWindow.read(close=True)
        
# if event == "drink":
#     n,values=drinkTypeWindow.read(close=True)
#     s,values=drinkSizeWindow.read(close=True)
#     i,values=drinkIceWindow.read(close=True)
#     drink=Drink(n,d[n+c[s]],s,i)
#     drinkConfirm=[
#     [sg.Text("Beverage {} Size {} with ice {} price $ {} to your order".format(n,s,i,d[n+c[s]]))],
#     [sg.Text("Do you want it to the order?")],
#     [sg.Button("Yes")],
#     [sg.Button("No")],
    
#     ]
    
#     drinkConfirmWindow=sg.Window(title="drinkConfirm",layout=drinkConfirm,margins=(100,50))
#     i,values = drinkConfirmWindow.read(close=True)
#     if event == 'Yes':
#         sg.popup("Items added to your order. Return to the main menu")
#         order.append(Drink(n,d[n+c[s]],s,i,))
#     else:
#         sg.popup("Items not discarded. Return to the main menu")
    



