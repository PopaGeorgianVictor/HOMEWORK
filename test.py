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