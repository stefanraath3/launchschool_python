'''
1. Add some code inside the following for loop to print the current value of num on each iteration. 
Before you execute the code: What sequence of numbers do you expect to be printed?

for num in range(0, 11, 2):
    pass # include your code here

------------------------------
------------------------------
2. The following code prints the numbers from 1 to 10. 
Modify it so that it instead prints the numbers from 10 to 1 in descending order, followed by 'Launch!'.

for i in range(1, 11):
    print(i)

------------------------------

for i in range(10, 1, -1):
    print(i)

print('Launch!')
------------------------------
------------------------------

3. Write a loop that prints the value of the greeting variable three times.

greeting = 'Aloha!'
------------------------------
greeting = 'Aloha!'

index = 1

while index <=3:
    print(greeting)
    index += 1

for _ in range(3):
    print(greeting)
------------------------------
------------------------------

4. Write a for loop that iterates over the integers from 1 to 100 
and prints the result of multiplying each integer by 2.

for element in range(1, 101):
    print(f'{element} * {element} = {element * 2}')

------------------------------
------------------------------

5. Using the code below as a starting point, 
write a while loop that prints the elements of lst at each index 
and terminates after printing the last element of the list.

lst = [1, 3, 7, 15]
index = 0
------------------------------

lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1
------------------------------
------------------------------

6. Your friends just showed up! Given the following list of names, use a for loop to greet each friend individually.
friends = ['Sarah', 'John', 'Hannah', 'Dave']
------------------------------

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for name in friends: 
    print(f'Hello, {name}!')
------------------------------
------------------------------

7. Write a for loop that iterates over the elements of the list cities 
and prints the length of each string. 
If the element is None, use the continue statement 
to skip forward to the next iteration without printing anything.

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

------------------------------

for city in cities: 
    if city is None:
        continue
    print(f'{city} has length ', len(city))
------------------------------
------------------------------
8. The following code keeps looping forever. 
(You can hit Ctrl-C to stop it.) 
Why does the loop keep running? Modify it so that it stops after the first iteration.
while True:
    print("and on")
------------------------------

while True:
    print("and on")
    break
------------------------------
9. Loop over the elements of the fish_list list below, logging each one. 
Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    if fish == 'Nemo':
        break
    print(fish)

index = 0

while index < len(fish_list):
    if fish_list[index] == 'Nemo':
        break
    print(fish_list[index])

    index += 1
------------------------------
------------------------------
10. Modify the following code so the loop continues iterating until the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input()
------------------------------

while True:
    answer = input('Should I stop looping? ')
    if answer == 'yes':
        break
'''

