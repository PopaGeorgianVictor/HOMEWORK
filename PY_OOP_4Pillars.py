


''' ABSTRACTION

        * abstract class: GeometricShape
        * contains a field PI=3.14
        * contains an abstract method area
        * contains a describe() class method - this prints to the screen 'The most I probably have corners'

   INHERITANCE

      * class Square - inherited GeometricShape
      * constructor for the side


   ENCAPSULATION
       * the side is private property
       * implement getter, setter, deleter for side
       * implements the method required by the interface

       Class Circle - inherits ShapeGeometric
            * radius constructor
            * range is private property
            * implement getter, setter, deleter for radius
            * implements the method required by the interface - in the calculation it uses field PI inherited from parent class

    POLYMORPHISM
        * define new method  describe() - print 'I have no corners'
        * create an object of type Square and play with its methods
        * create a Circle object and play with its methods



'''

from abc import ABC, abstractmethod

class GeometricShape(ABC):
	PI = 3.14

	@abstractmethod
	def area(self):
		pass

	def describe(self):
		print('The most I probably have corners')


class Square(GeometricShape):
	def __init__(self, side):
		self._side = side


	def set_side(self, side):
		self._side = side


	def get_side(self):
		return self._side


	def delete_side(self):
		del self._side
		print('Deleting..')
		print('The side of the square has been ERASED !!!')

	def area(self):
		return self._side ** 2


class Circle(GeometricShape):
	def __init__(self, radius):
		self._radius = radius


	def set_radius(self, radius):
		self._radius = radius


	def get_radius(self):
		return self._radius

	# deleter
	def delete_radius(self):
		del self._radius
		print('Deleting..')
		print('The radius of the circle has been ERASED !!!')

	def area(self):
		return self.PI * (self._radius ** 2)

	def describe(self):
		print("The most I probably don't have corners")


s = int(input('The square has sides of: '))
r = int(input('The circle has a radius of: '))

box = Square(s)
donut = Circle(r)

print(f"The side of the Square is: {box.get_side()}")
print(f"The area of the square is: {box.area()}")
print(f"The radius of the circle is: {donut.get_radius()}")
print(f"The area of the circle is: {donut.area()}")

print('-' * 100)

box.delete_side()
donut.delete_radius()