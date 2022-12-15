
'''class Circle(). Attributes: radius, color. Constructor for both attributes
     Methods:
      * circle_description() - will PRINT the color and radius
      * area() - return area
      * diameter() - return diameter
      * perimeter() - return perimeter'''




from math import pi


class Circle():
    def __init__(self,color,radius):
        self.color = color
        self.radius = radius

    def circle_description(self):
        print(f"The color of the circle is {self.color} and the radius is {self.radius} ")

    def object_like_circle(self):
        print(f'\tColor is {self.color}')
        print(f'\tRadius is {self.radius}')

    def area(self):
        return  f'Area is {pi * (self.radius)**2}'

    def diameter(self):
        return f'Diameter is {self.radius * 2}'

    def perimeter(self):
        return f'Perimeter is {2 * pi * self.radius}'




circle1 = Circle("RED", 5)
circle2 = Circle("GREEN", 7)

circle1.circle_description()
circle2.circle_description()
print('-' * 50)
print(circle1.area())
print(circle2.area())
print('-' * 50)
print(circle1.diameter())
print(circle2.diameter())
print('-' * 50)
print(circle1.perimeter())
print(circle2.perimeter())
print()

clock = Circle("PINK", 7)
coin = Circle("GOLD", 5)

print("My kinky clock have specification below: ")
clock.object_like_circle()
print(f"\t{clock.area()}")
print(f"\t{clock.diameter()}")
print(f"\t{clock.perimeter()}")
print()
print("My collectible coin have specification below: ")
coin.object_like_circle()
print(f"\t{coin.area()}")
print(f"\t{coin.diameter()}")
print(f"\t{coin.perimeter()}")




'''class Rectangle(). Attributes: length, width, color. Constructor for both attributes
     Methods:
      * rectangle_description() - will PRINT length, width, color
      * area() - return area
      * perimeter() - return perimeter
      * change_color() - this method returns nothing 
       It will take a new color as a parameter and override the attribute self.color
       You can check the color change by calling the method rectangle_description()
       '''

class Rectangle():
    def __init__(self,length, width, color):
        self.length = length
        self.width = width
        self.color= color

    def rectangle_description(self):
        print(f"The rectangle has the color {self.color}, the length is {self.length} and the width is shown as {self.width}")
    def object_like_rectangle(self):
        print(f'\tColor is {self.color}')
        print(f'\tLength is {self.length}')
        print(f'\tWidth is {self.width}')

    def area(self):
        return  f'Area is {self.width * self.length}'

    def perimeter(self):
        return f'Perimeter is {2 * (self.width * self.length)}'

    def change_color(self, new_color):
        self.color = new_color


d1 = Rectangle(5,2,"RED")
d2 = Rectangle(7,3,"GREEN" )
d1.rectangle_description()
d2.rectangle_description()
print('-' * 50)
print(d1.area())
print(d2.area())
print('-' * 50)
print(d1.perimeter())
print(d2.perimeter())
print('-' * 50)
d1.change_color('BLUE')
d2.change_color('BLUE')
d1.rectangle_description()
d2.rectangle_description()

print()

book = Rectangle(7,4,"RED")
table = Rectangle(100,50,"BROWN")

print("My favorite book have specification below: ")
book.object_like_rectangle()
print(f"\t{book.area()}")
print(f"\t{book.perimeter()}")
print()
print("My kitchen table have specification below: ")
table.object_like_rectangle()
print(f"\t{table.area()}")
print(f"\t{table.perimeter()}")
print()
print(f"Time has passed over my favorite book. Now, the new specifications are: ")
book.change_color("slight brown tint")
book.object_like_rectangle()






'''class Employee(). Attributes: surname, forename ,salary. Constructor for both attributes
     Methods:
      * employee_description() - will PRINT name, surname, salary
      * full_name() - return full name
      * monthly_salary() - return monthly salary
      * annual_salary() - return annual salary
      * salary_increase (percentage) - return salary increase'''


class Employee():
  def __init__(self,surname, forename ,salary):
    self.surname = surname
    self.forename = forename
    self.salary = salary

  def employee_description(self):
    print(f" The employee's surname is {self.surname}, forename is {self.forename} and his huge salary is {self.salary} $")

  def full_name(self):
    return f'Full name is {self.surname} {self.forename}'

  def monthly_salary(self):
    return f'The monthly salary with many zeros is {self.salary}'

  def annual_salary(self):
    return f'The extravagant annual salary is {self.salary * 12}'

  def salary_increase(self,percentage):
    salary_increase = self.salary + percentage * self.salary
    return  f'Cash flow is {salary_increase}'



employee1 = Employee("Steve", "Jobs", 100000000000)
employee2 = Employee("Elon","Musk",100000000000000000)

employee1.employee_description()
employee2.employee_description()
print('-' * 50)
print(employee1.full_name())
print(employee2.full_name())
print('-' * 50)
print(employee1.monthly_salary())
print(employee2.monthly_salary())
print('-' * 50)
print(employee1.annual_salary())
print(employee2.annual_salary())
print('-' * 50)
print(employee1.salary_increase(10/100))
print(employee2.salary_increase(10/100))







'''class Account(). Attributes: iban, account_holder ,sold. Constructor for both attributes
     Methods:
      * account_description() - will PRINT iban, account_holder ,sold
      * account_debit (amount) - return account debit 
      * account_credit (amount) - return account credit '''


class Account():
  def __init__(self, iban, account_holder ,sold):
    self.iban = iban
    self.account_holder = account_holder
    self.sold = sold

  def account_description(self):
    print(f'The holder {self.account_holder} has in the account {self.iban} the amount of {self.sold} ')

  def account_debit(self, amount):
    return f'The balance after debiting is {self.sold - amount}'

  def account_credit(self, amount):
    return f'The balance after crediting is {self.sold + amount}'




holder1 = Account("RO09PORL8297336485969785", "Steve Jobs", 1000000000000000000000)
holder2 = Account("RO25RZBR5749382385829154", "Elon Musk", 100000000000000000000000000000)
holder1.account_description()
holder2.account_description()
print('-' * 50)
print(holder1.account_debit(10000))
print(holder2.account_debit(10000))
print('-' * 50)
print(holder1.account_credit(1000000000000000000000))
print(holder2.account_credit(100000000000000000000000000000))








'''class Invoice(). Attributes: series, number, product_name, quantity, price_per_piece
     Constructor: all attributes, no series(will be constant, no builder needed, all invoices will
                  had the same series)
     Methods:
      * change_amount(amount)
      * change_price(price)
      * change_product_name(name)
      * generate_invoice() - will print tabular'''


from datetime import date
from tabulate import tabulate

class Invoice():
   series = 'INV242340'
   def __init__(self, number, product_name, quantity, price_per_piece):
      self.product_name= product_name
      self.number = number
      self.quantity = quantity
      self.price_per_piece = price_per_piece

   def change_quantity(self,quantity):
      self.quantity = quantity

   def change_price(self,price):
      self.price_per_piece = price

   def change_product_name(self,name):
      self.product_name = name

   def generate_invoice(self):
      print(f'Series: {self.series}')
      print(f'Number: {self.number}')
      print(f'Date: {date.today()}')
      print(tabulate([[self.product_name, self.quantity, self.price_per_piece, self.price_per_piece * self.quantity]],
                  headers=['PRODUCT', 'QUANTITY/kg', 'PRICE PER PIECE/lei', 'TOTAL']))


inv1 = Invoice(23, 'SMOKED SLANA', 2, 24)
inv2 = Invoice(46, 'RED ONION', 2, 2)
inv1.generate_invoice()
print('=' * 59)
inv2.generate_invoice()
print('=' * 56)
inv1.change_quantity(0.5)
inv1.change_price(10)
inv1.change_product_name('MICI')
inv1.generate_invoice()
print('=' * 56)
inv2.change_quantity(0.3)
inv2.change_price(20)
inv2.change_product_name('MUSTARD')
inv2.generate_invoice()








'''class Car(). Attributes: brand, model, max_speed, current_speed, color,
                            available_colors(set), enroll(bool)
     Constructor: model, max_speed
     Color = gray - all cars are gray when they leave the factory
             current_speed = 0 - all cars are standing still when they leave the factory
             available colors = you choose 5-7 colors
             brand = you choose - the factory produces only one brand but several models
             registered = False
     Methods:
            * describe() - will print all attributes except available_colors
            * enroll() - will change the enrolled attribute to True
            * paint(color) - will paint the car in the new color ONLY if 
            * the new color is in the available colors option, otherwise display an error 
            * accelerate(speed) - will accelerate to a certain speed, if the speed is 
                                  negative-error, if the speed is higher than max_speed 
                                  the car will accelerate to full speed
            * brake() - the car will stop and have speed 0'''




class Car:
   color = 'GRI'
   current_speed = 0
   available_colors = {'RED', 'YELLOW', 'BLUE', 'OCHER', 'FUCHSIA', 'CANDY PINK'}
   brand = 'DACIA'
   registered = False

   def __init__(self, model, max_speed):
      self.model = model
      self.max_speed = max_speed

   def describe(self):
      print(f"My favorite car is {self.brand} and the ideal model being {self.model} of a color {self.color}. At the moment I'm parked, I have {self.current_speed} km/h, but I'm thinking of hitting it with {self.max_speed}km/h and if the radar catches me, it's enroll {self.registered}")

   def enroll(self):
      self.registered  = True
      print(f'Now I ride legally: {self.registered} ')

   def paint(self, color):
      self.color = color
      if color in self.available_colors:
         print(f'The car has adopted the new color {self.color}')
      else:
         print('ACCES DENIED - paint unavailable')


   def accelerate(self, speed):
      if speed < 0:
         print('Hmmm, what do you mean negative speed!?')
      elif speed == self.max_speed :
         print('The maximum speed has been reached. For more power, activate the SUPER SONIC mode')
      elif speed > self.max_speed :
         print('SUPER SONIC mode has been activated')
      else:
         print("I'm not in a hurry, I'm thinking about the problem!")

   def brake(self):
      print(f"The car stopped, I have to refuel")
      self.current_speed  = 0

car1 = Car('LASTUN', 105)
car2 = Car('1300', 140)
car1.describe()
car2.describe()
print('-' * 100)
car1.enroll()
car2.enroll()
print('-' * 100)
car1.paint('MAGENTA')
car1.paint('RED')
car1.paint('CYAN')
car1.paint('YELLOW')
print('-' * 100)
car1.accelerate(-90)
car1.accelerate(105)
car1.accelerate(150)
car1.accelerate(5)
car2.accelerate(-70)
car2.accelerate(140)
car2.accelerate(190)
car2.accelerate(7)

print('-' * 100)
car1.brake()
car2.brake()




''' The TodoList class
Attributes: todo (dict, the key is the task name, the value is the description)
At the beginning we have no tasks, dict is empty and we don't need a constructor
Methods:
● add_task(name, description) - will be added to the dict
● complete_task(name) - will be deleted from the dict
● show_todo_list() - just the keys
● display_additional_details(task_name) - depending on the task name,
we print additional details.
○ If the task is not in the todo list, we ask the user if he wants it
add.
○ If he answers no - goodbye
○ If he answers yes - we ask him for task details and save name+details in
dict


'''









