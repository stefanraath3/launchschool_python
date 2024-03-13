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

------------------------------
------------------------------
3. Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

------------------------------
My Solution: 
'The Life of Brian',
A shallow copy of dict1 is being made with the dict constructor. When shallow copies are made, the outermost level
of the original object is copied. So in this case, since dict2 is a new variable in the stack, they are not the same object.
Changes to dict2 does not influence dict1 because they are distinct objects, even though they have the same values. 
dict2 was assigned dict1, so references to the same object weren't copied. in this case, dict2 is references a different 
object than dict1
------------------------------
------------------------------
4. Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])
------------------------------
My Solution: 
[1, 42, 3]
Changes made to the nested objects of dict1 will be reflected in dict2, because a shallow copy has been done of dict1 to 
create the object that dict2 references. These are two distinct objects, however their nested lists and tuples are not.
Only the heap memory addresses of the nested mutable objects were copied, and 
not the objects themselves. Therefore, dict1 and dict2 share the same references to the same nested objects at the same
heap memory locations. Thus, changes made to these nested objects will be reflected in both variables.

'''
