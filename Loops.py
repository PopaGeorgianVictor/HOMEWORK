

# 1. Given the list: cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
     # Use a for to iterate through the entire list and display:
       # my favorite car is x
       # do the same thing with using for each
       # do the same thing with using while


# using for

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for c in range(len(cars)):
    print('My favorite car is:  ', cars[c])



# using for each

for favorite_car in cars:
    print('My favorite car is:  ', favorite_car)


# using while

   # method  1

c = 0

while c < len(cars) :
    print('My favorite car is:  ' , cars[c] )
    c += 1


    # method 2

while True:
    print('My favorite car is:  ', cars[c])
    c += 1
    if c == len(cars) :
        break






# 2. Given the list: cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
     # use a for else inside a for
     # changes the items in the list so that they are written in uppercase,except the first and the last
     # in else print list

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for cars_upper in range(1, len(cars)-1):
   cars[cars_upper] = cars[cars_upper].upper()
else:
   print('cars_upper:', cars)






# 3. Given the list: cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
     # a buyer comes in who wants to buy a Mercedes
     # if the car is a Mercedes: print 'I found the car you wanted' else print 'I found the X car. I'm still looking'


cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

buyer_wish= 'Mercedes'

for car in cars:
    if car == buyer_wish:
        print('I found the car you wanted')
        break
    else:
        print(f"I found the {car} car. I'm still looking!")







# 4. Given the list: cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
     # a wealthy but indecisive buyer comes along. We will show him all the cars except Trabant and Lăstun
       # if the car is Trabant or Lăstun skip it (don't use else)
       # print 'You might like the X car'



cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

rich_buyer_avoid = ['Trabant', 'Lastun']
for car in cars:
    if car in rich_buyer_avoid:
        continue
    print(f'You might like the {car} car')






# 5. cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
     # Modernize the auto park:
       # create an empty list, old_cars
       # iterate through cars
       # when you find Lăstun or Trabant:
         # save this cars in old_cars
         # overwrite them with Tesla (in the initial cars list)
       # print 'Vintage cars are:'
       # print 'New models:'

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

old_cars = []

for i in range(len(cars)):
    if cars[i] in ['Trabant', 'Lastun']:
        old_cars.append(cars[i])
        cars[i] = 'Tesla'
print(f'Vintage cars are: {old_cars}')
print(f'New models: {cars}')






# 6. Given the dict:
# car_price = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }


   # A client comes with a budget of 15,000 $
     # shows only cars that fit this budget
     # iterate through dict.items() and access the car and price
     # print  'Your budget fits to buy:' else 'For a budget below 15,000 $ you can choose this car: '


car_price = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

budget = 15000

for car, car_price in car_price.items():
    if car_price >= budget:
        print('Your budget fits to buy: ', car)
    else:
        print('For a budget below 15,000 $ you can choose this car: ', car)







# 7. Given the list: nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]. Without using count show how many times 3 occurs


nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

count_number = 3
x = [i for i in nums if i == count_number]
print(f'The number {count_number} appears {len(x)} times')






# 8. Given the list: nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]. Without using sum ,calculates and displays the sum of numbers

nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

sum = 0

for num in nums:
    sum += num
print('The sum of the numbers is:', sum)






# 9. Given the list: nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3].  Without using max, display the highest number


nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

max_nr = 0
for nr in nums:
    if nr > max_nr:
        max_nr = nr
print(f'The maximum number is: {max_nr}')





# 10. Given the list: nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3].
      # if the number is positive, replace it with its negative value
      # print new list

nums = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for n in nums:
    if n >= 0:
        number_conversion = -n
        print(number_conversion)






# 11. Given the lists:
      # numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
      # even_number = []
      # odd_number = []
      # positive_number = []
      # negative_number = []

        # populates the other lists correctly
        # print all four list



nums = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_number = []
odd_number = []
positive_number = []
negative_number = []


for n in nums:
    if n % 2 == 0 :
        even_number.append(n)
    else:
        odd_number.append(n)
    if n >= 0:
        positive_number.append(n)
    else:
        negative_number.append(n)

print('Even numbers is:' , even_number)
print('Odd numbers is:' , odd_number)
print('Positive numbers is:' , positive_number)
print('Negative numbers is:' , negative_number)


# 12. Given the list: nums = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3].Without using sort, sort the list in ascending order


# nested for method

nums = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print ('Sorted list is: ' , nums)


# using while

nums = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

sorted_list= []

while nums:
    min = nums[0]
    for x in nums:
        if x < min:
            min = x
    sorted_list.append(min)
    sorted_list.remove(min)

print('Sorted list is: ' , sorted_list)



# 13. Number riddles:
      # secret_number = generate a random number between 1 and 30
      # guess_number = None
      # using while pick a number
      # python replies: Secret number it's bigger/Secret number it's smaller/Congratulations! You guessed it!



import random
while True:
  print('''1.I want to guess the number   2.I don't feel lucky ''')
  your_choice = int(input("Ce faci in continuare?\n"))
  if your_choice == 1:
    number = random.randint(1,30)
    break
secret_number = random.randint(1,30)
guess_number = int(input("Choose a number:"))
if secret_number == guess_number:
    print("Congratulations! You guessed it!")
else:
    if guess_number > secret_number:
        print("Secret number it's bigger")
    else:
        print("Secret number it's smaller")




# 14. Choose a number from the keyboard.Write a script to generate the following pyramid in the console:
      '''
1
22
333
4444
55555
666666
7777777'''

# method 1

number_of_rows = int(input("Pick numbers of rows:  "))

for i in range(number_of_rows + 1):
    for j in range(i):
        print(i, end='')
    print('')


# method 2

number_of_rows = int(input("Pick numbers of rows:  "))

for i in range(1, number_of_rows + 1):
    print(f'{str(i) * i}')



# 15. phone_keyboard = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]

   # print 'The current figure is'

phone_keyboard = [[1,2,3], [4,5,6], [7,8,9], [0]]
for key in phone_keyboard:
   for phone in key:
       print('The current figure is :', phone)









# 17. We imagine a football team
      # declare a list of 5 players
      # swaps_max = 3
      # swaps_done = you play with different values

      # if a certain player is already on the field and we still have changes available
        # make the change
        # removed player who you change it  from the list
        # add the entered player
        # displays x in, y out, z more changes

      # if the player is not on the field
        # print 'Can't make the change because player x is not in the field'
        # displays 'You still have z changes'



players = ['Ronaldo', 'Messi', 'Ronaldinho', 'Zidane', 'Maradona']
swaps_max = 3
swaps_done = 0
if swaps_done >= swaps_max:
    print('The maximum number of changes has been reached')
else:
    while swaps_done != swaps_max:
        print('=' * 100)
        print(f'Current players on the field are: {players}')
        print(f' {swaps_max - swaps_done} more changes can be made ')
        player_to_pop = input("The player entering the field is / or 'Q' for exit : ")
        if player_to_pop == 'Q':
            print("For now I don't want to make changes")
            break
        if player_to_pop not in  players:
            print(f'No change can be made because the player {player_to_pop} is not on the field')
            print(f'{swaps_max - swaps_done} more changes can be made ')
            continue
        else:
            swaps_done += 1
            players.remove(player_to_pop)
            player_to_add = input("The player entering the field is / or 'Q' for exit : ")
            if player_to_add == 'Q':
                print('Good day!')
                break
            players.append(player_to_add)
            print(f'Player {player_to_add} entered the field, player {player_to_pop} left the field, you have {swaps_max - swaps_done} more changes.')

        if swaps_done == swaps_max:
            print(f'The maximum number of changes has been reached')
            print('Have a nice day!')




