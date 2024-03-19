'''
1. What will the following code do and why? Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)
--------------
- it will create the variable my value, and assign it an int object of 20, because True will always be truthy
------------------------------
------------------------------
2. What will the following code do and why? Don't run it until you have tried to answer.
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

- I thought it wil print 15, but it seems that's not the case. 
- My understanding here was that python is using the same global variable x to do the reassignment
- but it seems like no, python actually creates a new local scope for x
- and the expression x + 5 is causing the error, because this x has not yet been initialised
------------------------------
------------------------------
3. What will the following code do and why? Don't run it until you have tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()

- it will print a
- but why?
- ah okay so variables initialised on the same block level, will be available inside that block 
------------------------------
------------------------------
4. What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()

- it will print 1, because a = 1 is initialised globally, which means that it is available in all scopes
------------------------------
------------------------------
5. What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

- I thought that it would print 1, because of the fact that we are using the print statement before the new local 
initialisation of a, but it seems like this is not the case!
- So python is basically detecting that we are creating a new local variable instance of a = 2, and sees that we are 
trying to print the value of a before it is assigned in the local scope 
------------------------------
------------------------------
6. What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

- I think it'll print 1, because the local a = 2 refers to a local instance of a, which is different from the global right?
a = 1

def my_function():
    a = 2
    print(id(a))
my_function()
print(id(a))
------------------------------
------------------------------
7. What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

- now in this case we are telling python to use the global instance of a, and reassign/change the pointer of the global a
to a new value once the function is called

a = [1]  # Use a mutable object like a list

def my_function():
    global a 
    print("Inside before modification:", a)
    a.append(2)  # Modify the global variable
    print("Inside after modification:", a)

print("Global before:", a)
my_function()
print("Global after:", a)
------------------------------
------------------------------
8. What will the following code do and why? Don't run it until you have tried to answer.

print(greeting)

greeting = 'Hello world!'

- it will raise an exception/error because we must always initialise a variable before we use it!
------------------------------
------------------------------
9. What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

- I initially thought that the value of a would change and therefore print(a) will log 17, but that's not the case!
- so when you use a variable as an argument to a function call, it is that object that this variable points to 
that becomes that value of the argument
- so therefore we are basically saying in this case, 'call my_function with the value of 7, and assign b accordingly'
- local var b in my_function is set to point to the same object as a
- integers are immutable!
- thus the right answer is that the print(a) will log 7
------------------------------
------------------------------
10. What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

- okay so I thougt that an error would be raised, but for this mutable object it doesn't seem like that's the case!
- Fascinating!
- So you can actually modify the mutable lists inside functions scopes

# Global mutable object
my_list = [1, 2, 3]

# Global immutable object
my_number = 10

def modify_list():
    # Directly modifying the content of the global mutable object
    my_list.append(4)

def change_number():
    global my_number  # Necessary to modify the global immutable object
    my_number = 20

print("Before:", my_list, my_number)
modify_list()  # This works without declaring 'my_list' as global
change_number()  # This requires 'global my_number'
print("After:", my_list, my_number)
------------------------------
------------------------------


'''

