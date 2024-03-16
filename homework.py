#Excercise 1

# "Example" -> 3
# "Hello World" -> 3
# "Brian" -> 2
# "This is a longer response" -> 8

# Vowels are: A, E, I, O, U

# create a space for user input
example = input("What is your name? ")
vowels = 0
# loop through the string
for letter in example:
# identify and count vowels
    if letter in 'aeiouAEIOU':
        vowels += 1
print(vowels)






# Excercise 2 


names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

# SYNTAX for List Comprehension
# newlist = [expression for item in iterable if condition == True]

newlist = [name.capitalize() for name in names1 if len(name) >= 4]
print(newlist)


#BONUS

names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
newlist = [name.capitalize() for name in names2 if len(str(name)) >= 4]
print(newlist)