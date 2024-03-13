'''
1. In your own words, explain the difference between these two expressions. 
my_object1 == my_object2
my_object1 is my_object2

------------------------------
My solution: 
The expression my_object1 == my_object2 asks the following: "are the values of the objects that 
these two variables point the same?", that is, we are basically asking whether the objects 
that they reference have the same value. So this line evaluates values.

For the expression my_object1 is my_object2 we are asking whether the variables point to the same object.
So the references of the variables are being compared. 

------------------------------
------------------------------

2. Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

the line set2 = set1 tells us that both variables set2 and set1 point to the same object in the heap.
therefore mutating that object with set1.add(range(5, 10)) will cause a subsequent change in set2.
both set1 and set2 share references to the same object, that is, they are aliases to that object in the heap.
Assigning set2 to set1 creates a new variable in the stack, with a new stack address, but doesn't create a new object
in the heap. instead it copies the reference from set1 into the target stack item of set2 so that both reference the same set
'''
