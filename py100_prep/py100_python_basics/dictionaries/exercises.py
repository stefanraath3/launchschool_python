'''
1. Create a dictionary that contains the following data, and assign it to a variable named car.
type	color	mileage
sedan	blue	80000

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80000,
}

print(car)
------------------------------
------------------------------
2. Add some code below the following code to define a year key with a value of 2003. 
Don't update the dictionary literal; instead, add some code after lines 1-5:

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car['year'] = 2003

print(car)
------------------------------
------------------------------
3. Using the following code, delete the 'mileage' key and its associated value from car.

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

del car['mileage']
print(car)
------------------------------
------------------------------
4. Using the following code, select and print the value 'blue' from the car object:
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(car['color'])
------------------------------
------------------------------
5. Calculate and print the number of key/value pairs in the following dictionary:

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(len(car))
------------------------------
------------------------------
6. Check whether the keys 'name' and 'grade' exist in the following dictionary:
student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)
print('grade' in student)
------------------------------
------------------------------
7. Create a nested dictionary that contains the following data.
Car

type	color	year
sedan	blue	2003

Truck

type	color	year
pickup	red	1998


vehicle = {
    'car' : {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },
    'truck' : {
        'type': 'pickup',
        'color': 'red',
        'year': 1908,

    },
}

print(vehicle)
------------------------------
------------------------------
8. Rewrite car as a nested list containing the same key/value pairs.

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

print(car)
------------------------------
------------------------------
9. Use a for loop to iterate over the numbers dictionary 
and return a list containing each number divided by 2. 
Assign the returned list to a variable named half_numbers and print its value using print.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

print(half_number) # [50, 25, 5]

> comprehension
half_numbers = [
    value // 2 for value in numbers.values()
]

print(half_numbers)

> for loop
half_numbers = []
for values in numbers.values():
    half_numbers.append(values // 2)

print(half_numbers)
------------------------------
------------------------------
10. Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

A high number is 100.
A medium number is 50.
A low number is 10.

for key, value in numbers.items():
    print(f'A {key} number is {value}')
------------------------------
------------------------------

'''
