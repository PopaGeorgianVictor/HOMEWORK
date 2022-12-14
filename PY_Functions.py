'''Function to calculate and return the sum of two numbers'''


def add_numbers(n1, n2):
    sum = n1 + n2
    return sum


num1 = float(input("First number is:  "))
num2 = float(input("Second number is: "))
print("Sum is: ", add_numbers(num1, num2))

'''Function to return TRUE if a number is even, FALSE for odd'''


def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


num_check = int(input("Number is: "))
print("Number is even? ", even_odd(num_check))

'''Function that returns the area of the rectangle'''


def rectangle_area(L, l):
    a = L * l
    return a


length = int(input("The length is : "))
width = int(input("The width is : "))

print('The area is: ', rectangle_area(length, width))

'''Function that returns the area of the circle'''

import math


def circle_area(radius):
    a = radiu s ** 2 * math.pi
    return a


raza_cerc = int(input("The radius of the circle is: "))
print('The area is: ', circle_area(raza_cerc))

'''Function that returns True if a character is found in the given string and False if not'''


def caracter(string):
    if ch in string:
        return True
    else:
        return False


ch = input('Character to  check is: ')
verificare_caracter = input("String is: ")
print("The character is found in the string?", caracter(verificare_caracter))

'''Function without return, receives a string and prints:
    # the number of lowercase characters
    # the number of upercase characters
'''


def string(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        else:
            c.islower()
            d["LOWER_CASE"] += 1

    print("The number of upercase characters : ", d["UPPER_CASE"])
    print("The number of lowercase characters  : ", d["LOWER_CASE"])


str = input('Give me the string: ')
string(str)

'''Function that receives a LIST of numbers and returns a LIST of only positive numbers'''


def positive_numbers(list):
    for j in range(total_numbers):
        if (list[j] >= 0):
            print(list[j], end='   ')


list = []
total_numbers = int(input("The total number of items in the list: "))
for i in range(1, total_numbers + 1):
    list_of_values = int(input(" Enter the value of the element %d  : " % i))
    list.append(list_of_values)

print("The positive numbers in the list are: ")
positive_numbers(list)

'''Function that returns nothing. Get two numbers and print:
     # the first number x is greater than the second number y
     # the second number y is greater than the first number x
     # numbers are equal'''


def num(num1, num2):
    if num1 > num2:
        print("{} it's greater".format(num1))
    elif num2 > num1:
        print("{} it's greater".format(num2))
    else:
        print('{} and {} are equals'.format(num1, num2))


num 1 = float(input('First numbers is: '))
num 2 = float(input('Second number is: '))
num(num1, num2)

'''Function that receives a month of the year and returns how many days that month has'''

from calendar import monthrange


def number_of_days_in_the_month(year, month):
    return monthrange(year, month)[1]


year = int(input("Year is:  "))
month = int(input("Month is: "))
print('Number of days in the month is: ', number_of_days_in_the_month(year, month))

'''Calculator function who return 4 values: sum, difference, multiplication,dividing of two numbers'''


def sum(x, y):
    return x + y


def difference(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def dividing(x, y):
    return x / y


nr1 = int(input("First number is: "))
nr2 = int(input("Second number is: "))
print("The operator is (+,-,*,/): ", end=" ")
choice = input()
if choice == '+':
    print("\n" + str(nr1) + " + " + str(nr2) + " = " + str(sum(nr1, nr2)))
elif choice == '-':
    print("\n" + str(nr1) + " - " + str(nr2) + " = " + str(difference(nr1, nr2)))
elif choice == '*':
    print("\n" + str(nr1) + " * " + str(nr2) + " = " + str(multiplication(nr1, nr2)))
elif choice == '/':
    print("\n" + str(nr1) + " / " + str(nr2) + " = " + str(dividing(nr1, nr2)))
else:
    print("\nInvalid operator")

'''Function that receives a list of digits (ie only 0-9).Returns a DICT that tells how many times each digit occurs'''


def frequency(list):
    DICT = {}
    for i in list:
        if (i in DICT):
            DICT[i] += 1
        else:
            DICT[i] = 1

    for key, value in DICT.items():
        print("% d : % d" % (key, value))


list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
frequency(list)

'''Function to receive a number and return the sum of all numbers from 0 to that number'''


def sumOfDigitsFrom0ToN(n):
    results = 0
    for i in range(n + 1):
        results += i
    return results


n = int(input("Number is: "))
print("Sum of total numbers from 0 to", n, "is", sumOfDigitsFrom0ToN(n))

'''Function that receives 2 lists of numbers (numbers can be duplicated). Return common numbers'''


# method 1

def common_numbers(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print('Common numbers are: ', a_set & b_set)
    else:
        print("No common elements found")


a = [1, 2, 3, 4, 5, 9]
b = [5, 2, 6, 7, 8, 9]
common_numbers(a, b)


# method 2

def common_numbers(a, b):
    a_set = set(a)
    b_set = set(b)

    if len(a_set.intersection(b_set)) > 0:
        return (a_set.intersection(b_set))
    else:
        return ("No common elements found")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_numbers(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_numbers(a, b))


# method 3

def common_numbers(a, b):
    results = [i for i in a if i in b]
    return results


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

print("Common numbers are: ", common_numbers(a, b))

'''Function to apply a price discount
If the product costs 100 lei and we apply a 10% discount. 
The price will be 90. Handle cases where the discount is invalid. 
For example, a discount of 110% is invalid.'''


def Discount(price, discount_percentage):
    discount = price * discount_percentage / 100
    discount = round(discount, 2)
    return discount


product = input("What is the product you want to buy? or X to exit!: ")
while product != "X":
    product_price = float(input("The price of the product is: "))
    discount_percentage = int(input("The discount applied to the product is:"))
    if discount_percentage > 100:
        print('Discount invalid')
    else:
        discount = Discount(product_price, discount_percentage)
        new_price = product_price - discount
        print("The price of the product after applying the discount: " + str(new_price))
        product = input("Do you want to buy another product? or X if you are on a diet")

'''Function to display the current date and time in different countries'''

from datetime import datetime
import pytz


def country_time_zones():
    Country_Zones = ['America/New_York', 'Asia/Kolkata', 'Australia/Sydney',
                     'Canada/Atlantic', 'Brazil/East', 'Chile/EasterIsland', 'Cuba', 'Egypt',
                     'Europe/Amsterdam', 'Europe/Athens', 'Europe/Berlin', 'Europe/Istanbul',
                     'Europe/Jersey', 'Europe/London', 'Europe/Moscow', 'Europe/Paris',
                     'Europe/Rome', 'Hongkong', 'Iceland', 'Indian/Maldives', 'Iran',
                     'Israel', 'Japan', 'NZ', 'US/Alaska', 'US/Arizona', 'US/Central',
                     'US/East-Indiana', 'Europe/Bucharest']
    country_time_zones = []
    for country_time_zone in Country_Zones:
        country_time_zones.append(pytz.timezone(country_time_zone))
    for i in range(len(country_time_zones)):
        country_time = datetime.now(country_time_zones[i])
        print \
            (f"Date from {Country_Zones[i]} is {country_time.strftime('%d-%m-%y')} and the time is {country_time.strftime('%H:%M:%S')}")


country_time_zones()

''' Function to display how many days are left until Christmas'''

from datetime import date
def x_mas_counting():
    x_mas_day = date(date.today().year, 12, 25)
    current_day = date.today()
    left = x_mas_day - current_day
    print (f"Today we are on {current_day}, Christmas it's just over {x_mas_day}, so you still have {left.days} days to wait")


x_mas_counting()
