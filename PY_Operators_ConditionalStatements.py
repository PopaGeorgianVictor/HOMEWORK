
'''Checks and displays whether x is a natural number or not'''

# isnumeric method

x = input("Enter the number: ")
if x.isnumeric():
    print(f"The number {x} is natural number")
else:
    print(f"The number {x} is not a natural number ")


# check condition: natural numbers are strictly positive integers

x = float(input("Enter the number: "))
if x > 0 and type(x)==int:
    print(f"The number {x} is natural number")
else:
    print(f"The number {x} is not a natural number")







'''Checks and displays whether x is a positive, negative, or neutral number'''

# using if-elif-else statement

x = float(input("Enter the number: "))
if x > 0:
   print(f"Number {x} is positive")
elif x < 0:
   print(f"Number {x} is negative")
else:
   print(f"Number {x} is neutral")


# list comprehension

n = float(input("Enter the number:  "))
x = ["positive" if n>0 else "negative" if n<0 else "zero" ]
print(x)







'''Checks and displays if x is between -2 and 13'''

# check if the number is greater than -2 and less than 13

x = int(input("Enter the number: "))
if x > -2 and x < 13:
    print(f"Number {x} is in the range")
else:
    print(f"Numarul {x} is not in the range")


# list comprehension

x = int(input("Enter the number: "))
n = ['in the range' if x > -2 and x < 13 else 'not in the range']
print(n)

# with range() function

nr = range(-2,13)
number = int(input('Enter the number: '))

if number in nr:
    print(number, ' is in the range')
else:
    print(number, 'is not in the range')








''''Checks if x is NOT between 5 and 2'''

# check if the number is not greater than 5 and not less than 27

x = int(input("Enter the number:  "))
if not (x > 5 and x < 27):
   print(f"Number {x} is not in the range")
else:
   print(f'Number {x} is in the range')



# list comprehension

x = int(input("Enter the number:  "))
n = ['is not in the range' if not (x > 5 and x < 27) else 'is in the range']
print(n)



# with range() function

interval = range(5,27)
nr = int(input('Enter the number: '))
if nr not in interval:
    print(nr, 'is not in the range')
else:
    print(nr, 'is in the range')








 '''x, y-int. Checks and displays if they are equal, if not displays which one is greater'''

# if-else statement

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

if x == y :
    print('The numbers are equal')
else:
    if x > y :
        print (x,'is the bigger number')
    else:
            print(y,'is the bigger number')


# if-elif-else statement

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

if x == y :
    print('The numbers are equal')
elif x > y :
    print(x, 'is the bigger number')
else:
    print(y, 'is the bigger number')






'''x,y,z - the sides of a triangle. Check whether a Triangle is Equilateral, Isosceles or Scalene'''

# if-elif-else statement

print("Enter the lengths of each side")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
   print("The triangle is equilateral")
elif x==y or y==z or z==x:
   print("The triangle is isosceles")
else:
   print("The triangle is scalene")





'''Check and display if it is vowel or not'''


# lower() method

letter = input('Litera este :')
vowel  = "aeiou"

if letter[0].lower() in vowel:
    print('The letter is a vowel')
else:
    print('The letter is a consonant')


# list comprehension

letter = input('Litera este :')
vowel  = "aeiou"

w = [ 'The letter is a vowel' if letter[0].lower() in vowel else 'The letter is a consonant' ]
print(w)







'''Convert and print notes from the Romanian system to >
Over 9 => A
Over 8 => B
Over 7 => C
Over 6 => D
Over 4 => E
4 or below => F'''

nota = int(input("Enter a note from the Romanian system: "))
if nota > 9:
    print(f"The grade {nota} is represented by A")
elif nota >= 8:
    print(f"The grade {nota} is represented by B")
elif nota >= 7:
    print(f"The grade {nota} is represented by C")
elif nota >= 6:
    print(f"The grade {nota} is represented by D")
elif nota > 4:
    print(f"The grade {nota} is represented by E")
else:
    print(f"The grade {nota} is represented by F")







'''Checks if x has at least 4 digits'''

# len() function

x = int(input("The value of x is: "))
if len(str(x)) >= 4:
   print(f"Number  {x} has {len(str(x))} digits")
else:
   print(f"Number {x} does not have a minimum of 4 digits")


# list comprehension

x = int(input("The value of x is: "))
n = [f"Number  {x} has {len(str(x))} digits" if len(str(x)) >= 4 else f"Number {x} does not have a minimum of 4 digits" ]
print(n)








'''Checks if x has exactly 6 digits'''

#  len() function

x = int(input("The value of x is :"))
if len(str(x)) == 6:
   print(f"The number {x} has exactly 6 digits")
else:
   print(f"The number {x} does not have exactly 6 digits")


#  list comprehension


x = int(input("The value of x is :"))
n = [f"The number {x} has exactly 6 digits"  if len(str(x)) == 6 else f"The number {x} does not have exactly 6 digits"]
print(n)







'''Checks whether x is odd or even'''

# modulo operator

x = int(input("Enter the first number: "))
if x % 2 == 0:
  print (f'The number {x} is an even number')
else:
    print(f'The number {x} is an odd number')


# list comprehension

x = int(input("Enter the first number: "))
n =[f'The number {x} is an even number' if x % 2 == 0 else f'The number {x} is an odd number']
print(n)








'''x,y,z - int. Show which one is the biggest?'''


# using just if !

x = int(input('First number is:  '))
y = int(input('Second number is:  '))
z = int(input('Third number is:  '))

the_largest_number = 0

if x > y and x > z:
    the_largest_number = x
if y > x and y > z:
    the_largest_number = y
if z > x and z > y:
    the_largest_number = z

print(the_largest_number , "is the biggest")


# if-else statement

x = int(input("What is the value of x:  "))
y = int(input("What is the value of y:  "))
z = int(input("What is the value of z:  "))

if x >= y:
    if x >= z:
        print(f"The biggest is: {x}")
    else:
        print(f"The biggest is: {z}")
else:
    if y >= z:
        print(f"The biggest is: {y}")
    else:
        print(f"The biggest is: {z}")







'''x,y,z -represent the angles of a triangle. Checks and displays whether the triangle is valid or not'''

# if-else statement

x = int(input('First angle is: '))
y = int(input('Second angle is : '))
z = int(input('Third angle is : '))

if x + y + z == 180 and x != 0 and y != 0 and z != 0:
    print("The angles are congruent to form a triangle")
else:
    print("The angles are not right to form a triangle")


# list comprehension

x = int(input('First angle is: '))
y = int(input('Second angle is : '))
z = int(input('Third angle is : '))

a = ["The angles are congruent to form a triangle" if x + y + z == 180 and x != 0 and y != 0 and z != 0 else  "The angles are not right to form a triangle"]
print(a)






''' Given the string: 'Coral is either the stupidest animal or the smartest rock'
      # read an int x from the keyboard
      # display the string without the last x characters
      # declare a new string consisting of the first 5 characters + last 5'''


coral_my_favorite_animal = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("x is : "))
print(coral_my_favorite_animal[:- x])

new_coral_my_favorite_animal = coral_my_favorite_animal[:5] + coral_my_favorite_animal[-5:]
print(new_coral_my_favorite_animal)







'''  Given the string: 'Coral is either the stupidest animal or the smartest rock'
      # save to a variable and display the start index of the word rock
      # using this variable + slicing, display the entire string up to this one word
'''

coral_my_favorite_animal = 'Coral is either the stupidest animal or the smartest rock'
word = 'rock'
word_index = coral_my_favorite_animal.index(word)
print(coral_my_favorite_animal[:word_index])







'''Read a string from the keyboard.Checks if the first and last characters are the same'''

# assert method

x = input('Your favorite word is: ')
assert  x[0].capitalize() == x[-1].capitalize(), 'the first and last character are different'







'''
  Given the string:  '0123456789'
      # show even numbers only
      # show only odd numbers
'''

str = '0123456789'
print(f"Even numbers are: {str[::2]}")
print(f"Odd numbers is: {str[1::2]}")





'''Guess the dice game:

* we imagine you roll the dice and save this number in dice_roll
* take a guessed number from the user
* check and display if the user guessed

You will have 3 options
● You lost. You chose a smaller number. You chose x but it was y
● You lost. You chose a higher number. You chose x but it was y
● You guessed it. Congratulations! You chose x and the die was y


'''

# method 1

import random
dice_roll = random.randint(1,6)
guess =  int(input("Guess the number from dice roll: "))
if guess == dice_roll:
    print(f"I played and chose {guess} and the dice was {dice_roll}, I won!")
else:
    if guess > dice_roll:
        print(f"You are a failure. You chose a higher number. You chose {guess} but the die was {dice_roll}")
    else:
        print(f"You are a failure.You chose a smaller number. You chose {guess} but the die was {dice_roll}")





