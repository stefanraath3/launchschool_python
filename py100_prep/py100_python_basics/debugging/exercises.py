'''
1. You come across the following code. What errors does it raise for the given examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

- We are going to have TypeErrors, because in our function definition we have specified only a single positional parameter, but in the
call 6 are given
- for the second function call, we are calling it in a non-iterable datatype, an integer
------------------------------
------------------------------
2. Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. 
However, the output is the same every time the function is invoked. 
Why? Fix the code so that it behaves as expected.

import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

- when the function is called it will continually print the same output, because our conditonal is checking whether the value of the sunshine 
variable is truthy, and in our case, the arguments provided are strings. All non-empty strings are truthy, so when the function is called
the random.choice function chooses a non-empty string, which results in our condition always evaluating to truthy, and therefore our outputs 
in the first if block always gets executed. the else block code only gets executed if sunshine is falsy. 
- so to fix this, we just need to remove the strings from the random.choice() argument, and instead use the boolean literals True and False

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
------------------------------
------------------------------
3. When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")
- the result is not what we expect because the number = input() takes the user input as a string
- therefore the n * 5 returns the string concatenated 5 times
- to fix this we need to coerce the user input into an int

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")
------------------------------
------------------------------
4. Magdalena has just adopted a new pet! 
She wants to add her new dog, Bowser, to the pets dictionary. 
After doing so, she realizes that her dogs Sparky and Fido have been mistakenly removed. 
Help Magdalena fix her code so that all three of her dogs' names will be associated with the key 'dog' in the pets dictionary.

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }


(pets['dog'].append('bowser'))

print(pets['dog'])
------------------------------
------------------------------
5. You want to have a small script delivering motivational quotes, 
but with the following code you run into a very common error message: 
TypeError: can only concatenate str (not "NoneType") to str. 
What is the problem and how can you fix it?

def get_quote(person):
    if person == 'Yoda':
        'Do. Or do not. There is no try.'
    if person == 'Confucius':
        'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')


- to fix this we need to add return statements because without them the function is returing None, and you can't concatenate NoneType with strings
def get_quote(person):
    if person == 'Yoda':
       return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
       return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
       return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Einstein') + '"')
------------------------------
------------------------------
6. You want to add the numbers from 1 to 5 to a list, 
but the code below is not producing the expected result. 
How can you fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

- the issue is with the iterator part. so here we see that range(5) produces a range object that starts at 0, and ends just before 5
- what we want is to change the arguments of the range constructor such that it starts at 1, and ends at one after 5, 6

numbers = []

for i in range(1,6):
    numbers.append(i)

print(numbers)
------------------------------
------------------------------
7. You are trying to access a value in a dictionary, 
but the code is giving you an error. 
Can you change line 3 so that it prints "Unknown" instead of raising an error?

info = {'name': 'Srdjan', 'age': 38}

print(info['city'])

- the issue is that we're using key based access here, which will return a keyerror if the key is not present
- instead we gotta use the .get() method, with the key as first argument, and the return value of 'Unkown' as second
print(info.get('city', 'Unkown'))
------------------------------
------------------------------
8. We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. 
However, we encountered an issue, 
as whenever we change a value in one nested list, all nested lists are affected. 
Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


- hmmm okay so i used the deep copy method, but a more straightforward way would be to use just the .copy() method!
import copy
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(copy.deepcopy(sub_list))

matrix[0][0] = "X"
print(matrix)

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix)
------------------------------
------------------------------
9. Your colleague has implemented a custom function to find the maximum value in a list. 
However, the function sometimes works correctly, but other times it produces incorrect results. 
Can you help your colleague fix the bug?

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

- okay so I knew the issue was the 0, but hmmm i thought we could use the max() and min() functions on the lists
def find_maximum(numbers):
    if not numbers:
        return None
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = max(numbers)
        if number < max_number:
            max_number = max(numbers)
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

- but let's explain the following answer
def find_maximum(numbers):
    if not numbers:
        return None

    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

-aaah okay I see
- so it looks like we are choosing a number that is inside the list, and then comparing that number with every subsequent number produced
by the iteration
- for every iteration that the number is not greater than the initial number, it skips the assignment 
- for every number greater than, it does the assignment, and moves on the compare with the next
------------------------------
------------------------------
10. You've been asked to implement a function called digit_product 
that takes a string of digits as an argument 
and returns the product of all the digits in the string.
When testing the function, 
you find that it returns 0, which is not what you expect. 
Can you identify the issue and correct the code?

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 0

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0


'''

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('212345')
print(result)  # expected: 120, actual: 0

