


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
    def __int__(self, side):
        self._side = side


    @property
    def side(self):
        return self._side


    @get_side.getter
    def get_side(self, side):
        if side > 0:
            self._side = side
            return self._side
        else:
            print('Side length is not valid')


    @set_side.setter
    def set_side(self, side):
        self._side = side


    @delete_side.deleter
    def delete_side(self):
        print('Deleting..')
        del self._side
        print('The side of the square has been ERASED !!!')


    def area(self):
        return self._side ** 2



class Circle(GeometricShape):
    def __int__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @get_radius.getter
    def get_radius(self):
        return self._radius


    @set_radius.setter
    def set_radius(self, radius):
        self._radius = radius

    @delete_radius.deleter
    def delete_radius(self):
        print('Deleting..')
        del self._radius
        print('The radius of the circle has been ERASED !!!')

    def area(self):
        return self.PI * (self._radius ** 2)

    def describe(self):
        print('The most I probably have corners')




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