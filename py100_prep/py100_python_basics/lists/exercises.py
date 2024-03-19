'''
1. Write a function that returns the first element of a list provided as an argument. For example:

print(first(['Earth', 'Moon', 'Mars']))  # Earth

def first(list):
    if len(list) != 0:
        return list[0]
    else:
        return 'Empty List'


print(first([]))

- hmmm okay so a better way to go about doing this is to ask
how can we write this in more Pythonic way

- so instead of doing the whole check if the len is not empty, just take advantage of the fact that a non-empty list
is truthy

so a better function definition would be:
def first(list):
    if list:
        return list[0]
    else:
        return None

print(repr(first([' '])))
------------------------------
------------------------------
2. Write a function that returns the last element of a list provided as an argument. For example:
print(last(['Earth', 'Moon', 'Mars']))  # Mars

def last(str):
    if str:
        return str[-1]
    else:
        return None

print(last(['Earth', 'Moon',]))  # Mars
------------------------------
------------------------------
3. We are given the following list of energy sources. 
Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.remove('fossil')
energy.append('geothermal')

print(energy)
------------------------------
------------------------------
4. Split the string alphabet into a list of characters.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(list(alphabet))
------------------------------
------------------------------
5. Count the number of elements in scores that are 100 or above.
scores = [96, 47, 113, 89, 100, 102]
count_list = [ 
    number for number in scores
    if number >= 100
]

print(len(count_list))
------------------------------
------------------------------
6. You've been given a list of vocabulary words grouped into sub-lists, by meaning. 
This is a two-dimensional list or a nested list. 
Write some code that iterates through and prints all the words, one per line.

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]


for sublist in vocabulary:
    for word in sublist:
        print(word)
------------------------------
------------------------------
7. Predict the output of the code shown below. 
When you run the code, do you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)
- the output will be True, because list1 == list2 is asking us whether the objects that these vars point to have the same values
------------------------------
------------------------------
8. How can you check if a variable holds a value that is a list? 
Given two variables, verify whether the values they hold are lists.

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(type(some_value1) is list)
print(type(some_value2) is list)
------------------------------
------------------------------
9. The destinations list contains a list of travel destinations.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

Write a function that, without using the built-in in operator, 
checks whether a specific destination is included within destinations. 
For example: When checking whether 'Barcelona' is contained in destinations, 
the expected output is True, whereas the expected output for 'Nashville' is False.

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

def contains(country, destination_list):
    for member in destination_list:
        if country == member:
            return True
            break
        else:
            return False
  
print(contains('Barcelona', destinations))
------------------------------
------------------------------
10. We generated parts of a passcode 
and now want to combine them into a string. 
Write some code that returns a string, 
with each portion of the passcode separated by a hyphen (-).

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

print('-'.join(passcode))
------------------------------
------------------------------
11. We have a grocery list. 
As we check off items on that list, we want to remove them from the list.
Write code that removes the items from grocery_list, 
one by one, until it is empty. 
If you print the elements you remove, 
the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']


while grocery_list:
    print(grocery_list.pop())

print(grocery_list)

paprika
tofu
garlic
quinoa
carrots
broccoli
hummus
[]
'''
