
'''Declare a list of musical notes
     # display it
     # reverse the order using slicing and overwrite the list
     # print the current version (inverted)
     # on this list apply a method that you suspect does the same thing,that is, to reverse its order. You don't need to overwrite it in this case because the method does this automatically
     # print the current version of the list. You are basically back to the variant initial'''


# slicing , reverse and overwrite

musical_notes = ['DO' , 'RE' , 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO']
print(musical_notes)
arpeggio = musical_notes[::-1]
print(arpeggio)
arpeggio.reverse()
print(arpeggio)







''' Same musical notes list. How many times does 'do' appear?'''

# counting the 'do'

musical_notes  = ['DO' , 'RE' , 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO']
count_DO = musical_notes.count('DO')
print(count_DO)








''' Having 2 lists: [3, 1, 0, 2] and [6, 5, 4]. Join them in one list'''

# concatenation (+) operator

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
ls = list1 + list2
print(ls)

# extend method

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list1.extend(list2)
print(list1)

# append() method

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
for x in list2 :
    list1.append(x)
print(list1)

# ‘*’ operator

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
res = [*list1, *list2]
print ("Concatenated list:\n " + str(res))


# itertools.chain() method

import itertools

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
res = list(itertools.chain(list1, list2))

print("Concatenated list:\n " + str(res))

# list comprehension

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
res = [j for i in [list1, list2] for j in i]
print ("Concatenated list:\n"+ str(res))







''' Having 2 lists: [3, 1, 0, 2] and [6, 5, 4]
     # concatenate the lists
     # sort the list (ascending and descending)
     # remove 0
     # print new list
'''

ls = list1 + list2
ls.sort() , print('Ascending sorted list is', ls)
ls.sort(reverse = True) , print('Descending sorted list is', ls)
ls.remove(0) , print('New list is', ls)







''' Having 2 lists: [3, 1, 0, 2] and [6, 5, 4]. Concatenate the lists and check if list is empty or not'''

# if - not - else

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
ls = list1 + list2

if not ls:
    print('list is empty')
else:
    print('list is not empty')


# if - len - else

if len(ls) == 0:
    print('list is empty')
else:
    print('list is not empty')







''' Having 2 lists: [3, 1, 0, 2] and [6, 5, 4].Concatenate the lists and delete list and check if list is empty'''


# clear method

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
ls = list1 + list2

ls.clear()
check = ['list is empty' if not ls else 'list is not empty']
print(check)







''' Having the dictionary {'Ana' : 8, 'George' : 10, 'Alex' : 5}
     # display only names
     # names are students and digits are grades.Print students and a grade for each one
     # Alex appealed and got 6.Change Alex's grade to 6 and print it
     # George transfers from the class.In place of George comes Isabela with grade 9.Print new dictionary'''

# keys and pop method

d = {'Ana' : 8, 'George' : 10, 'Alex' : 5}

print(d.keys())

for key in d.keys():
    print( key, 'took grade ' , d[key])

d['Alex'] = 6
print('Congrats Alex, you got ' , d['Alex'])

d.pop('George')
d['Isabela'] = 9
print('New students and grade are' , d)









'''# Having the sets: weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'} and weekend = {'Saturday','Sunday'}
     # check condition: sets cannot contain duplicates. Duplicates are discarded when initializing a set
     # check if weekend is a subset of weekdays or not
     # show the differences between sets
     # show the intersection of elements between sets'''

weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
weekend = {'Saturday','Sunday'}

weekend.add('Monday')
print('Condition checked:', weekdays)

# issubset method

subset = ['weekend is a subset of weekdays' if weekend.issubset(weekdays) else 'weekend is not a subset of weekdays']
print(subset)

# difference method - if we have equal sets then it will return the null set

print(weekend.difference(weekdays))

# intersection method

print(weekend.intersection(weekdays))


