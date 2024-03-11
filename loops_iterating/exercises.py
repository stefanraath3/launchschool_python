'''
4. Use a while loop 
to print all numbers 
in my_list with even values, 
one number per line. 

Then, print the odd numbers using a ' for' loop.

Expected even values 
6
0
20
4

Expected Odd Values
3
11
17
'''
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):
    if (my_list[index] % 2 == 0):
        print(my_list[index])
    index += 1

for number in my_list:
    if number % 2 != 0:
        print(number)
    