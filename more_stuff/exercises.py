'''
1. What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
------------------------------
Solution: 
CHRIS

dictionary.keys() creates a dictionary view of keys
Composition is used to create a sorted list of this view
chaning is used to access the second element at index 1
and transform that element key into uppercase

------------------------------
------------------------------
2. Use the sqrt function from the math library to write some code 
that outputs the square root of 37. 
Try to write the code in three different ways.

------------------------------
Solution: 
import math

print(math.sqrt(37))
-

import math as m
print(m.sqrt(37))
-
from math import sqrt

print(sqrt(37))

------------------------------
------------------------------
3. Consider the following code:

def sum_of_squares(num1, num2):
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

Write a nested function in sum_of_squares that will make this code work as shown.
------------------------------
Solution: 

def sum_of_squares(num1, num2):
    def square(num):
        return num * num
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))  
print(sum_of_squares(5, 12))  
------------------------------
------------------------------
4. Write a function called increment_counter 
that increments a counter variable every time it is called. 
You can test your code with the following:

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

------------------------------
Solution:
counter = 0

def increment_counter():
    global counter 
    counter += 1
    return counter

increment_counter()
print(counter)

increment_counter()
print(counter)  

counter = 100
increment_counter()
print(counter)
------------------------------
------------------------------

'''
