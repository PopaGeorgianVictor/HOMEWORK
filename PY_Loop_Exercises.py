
'''
Problem 1
Given a list (my_words) that has words as its elements, write a loop that will print out
only the words that are 5 or more letters long. For example your code will not print the word 'ok' but it
will print the word 'Python'.

'''




my_words = ['Python', 'ok', 'selenium', 'integer', 'java', 'loop', 'webdriver', 'yes', 'Interactive']

for word in my_words:
    if len(word) >= 5:
        print(word)





'''
Problem 2
Take the same list in problem 1, instead of printing the words that meet the criteria, add them to a new list called 'my_new_words'
and print the list.
'''


my_words = ['Python', 'ok', 'selenium', 'integer', 'java', 'loop', 'webdriver', 'yes', 'Interactive']

my_new_words = []
for word in my_words:
    if len(word) >= 5:
        my_new_words.append(word)

print(my_new_words)





'''
Problem 3
Using a while loop print the string "abc" 10 times. Also print the count right after the string on the next line. Do not use a 'for' loop.
Hint: use a counter variable
'''



counter = 1
while counter <= 10:
    print ("abc")
    print ("count is %d" % counter)
    counter += 1





'''
Problem 4
Given the dictionary 'population', which is city and population pair, iterate the the dictionary and print only the cities
with population more than 1.5 million. 
'''




population = {'New York': 8.5, 'San Jose': .9, 'Phoenix': 1.6, 'Houston': 2.2, 'Chicago': 2.7, 'San Antonio': 1.3}

for key, value in population.items():
    if value > 1.5:
        print("Cities with population more than 1.5 million are: " , key)





'''
Problem 5
Given list of cities 'cities', iterate through the list and print the cities that population information is available in
the dictionary 'population'.
Example: Oakland will not be printed but Phoenix will be printed
'''



cities = ['Oakland', 'Phoenix', 'Houston', 'New Mexico', 'Chicago', 'Boston', 'Los Angeles', 'San Jose']
population = {'New York': 8.5, 'San Jose': .9, 'Phoenix': 1.6, 'Houston': 2.2, 'Chicago': 2.7, 'San Antonio': 1.3}


for city in cities:
    if city in population.keys():
        print("Cities with available population information are:" , city)





'''
Problem 6
Given list of cities 'cities', and dictionary population, iterate though the list and print the city and population as
 shown in the example. If the population information is not available print "Population information not available for : <the city name>
 Example:
 >>> Chicago --> 2.7
 >>> Population information not available for : Oakland

'''



cities = ['Oakland', 'Phoenix', 'Houston', 'New Mexico', 'Chicago', 'Boston', 'Los Angeles', 'San Jose']
population = {'New York': 8.5, 'San Jose': .9, 'Phoenix': 1.6, 'Houston': 2.2, 'Chicago': 2.7, 'San Antonio': 1.3}


for city in cities:
    if city in population.keys():
        city_population = population[city]
        print (f"Here is population information for the requested cities {city} ----> {city_population}")
    else:
        print ("Population information not available for :" ,  city)




'''
Problem 7
Its snack time and we want to decide 3 fruits to eat from the available food in the kitchen.
All available foods in the kitchen are in the list 'available_foods', and foods considered fruits are in the list 'fruits'.
Iterate through the available foods list and print only 3 fruits for snack.
Hint: Stop printing as soon as you find 3 foods considered fruit.
'''



available_foods = ['cheese', 'banana', 'orange', 'chicken', 'beef', 'apple', 'burrito', 'pizza', 'mango', 'pineapple', 'papaya', 'ham']
fruits = ['orange', 'mango', 'papaya', 'pineapple', 'banana', 'apple', 'peach', 'grape', 'avocado', 'pear']

counter = 0
for food in available_foods:
    if food in fruits:
        print(f'Just {food} for today')
        counter += 1

    if counter == 3:
        break





'''
Problem 8
Given the list 'collection' print every single word in the list. The list contains another list that contains words. Print all
of the words.
'''



collection = ['python', 'qa', 'selenium', ['java', 'ruby', 'pearl', 'c++'], 'dell', 'toshiba' ]

# type method

for i in collection:
    if type(i) == list:
        for j in i:
            print(j)
    else:
        print(i)




# isinstance method

for i in collection:
    if isinstance(i, list):
        for j in i:
            print(j)
    else:
        print(i)


