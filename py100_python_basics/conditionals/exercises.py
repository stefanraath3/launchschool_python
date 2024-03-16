'''
1. Without looking at your notes or the official documentation, try to recall all values that count as falsy in Python.
- False 
- NoneType
- All numeric zeros
- empty strings ''
- empty collection types like set(), dict(), tuple(), frozenset(), range(0)
- custom classes that are defined as zero
------------------------------
------------------------------
2. The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.
Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.
import random
random_number = random.randint(0, 1)

if random_number == 1:
    print(f'{random_number} Yes!')
elif random_number == 0:
    print('No!')
------------------------------
------------------------------

3. Rewrite your code from the previous exercise to use a ternary expression.
import random
random_number = random.randint(0, 1)
print('Yes') if random_number == 1 else print('No')
------------------------------
------------------------------
4. Initialize a variable weather 
with a string value being 'sunny', 'rainy', or whatever weather condition you choose.
 Then, write an if statement that prints:

It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else
Test your code with different values for weather.
------------------------------

weather = 'rainy'

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("I'ts still a beautiful day! Grab that umbrella")
else:
    print("let's stay inside")
------------------------------
------------------------------
5. Examine the code shown below. Without running it, determine what it will print. 
animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

------------------------------
- it'll print 'neigh'

------------------------------
------------------------------
6. Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. 
Feel free to add more cases besides 'sunny' and 'rainy'.

weather = 'rainy'

match weather:
    case 'sunny':
        print('sunny day!')
    case 'rainy':
        print('yah! water from sky')
    case 'snowy':
        print('fluffy!!')
    case _:
        print('stay inside')

------------------------------
------------------------------
7. Predict the output of the following code:
if False or True:
    print('Yes!')
else:
    print('No...')

Will always be Yes! because the or conditional evaluates to True if either operand is truthy, and True is truthy
------------------------------
------------------------------
8. Predict the output of the following code:
if True and False:
    print('Yes!')
else:
    print('No...')

Will always be No... because conditional evaluates to falsy, because and needs both operands to be truthy
------------------------------
------------------------------
9. Without running the following code, determine what will be printed.
sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

3.99, because the ternary expression evaluates such that the else statement is excuted and admission_price becomes 3.99. 
the sale is True, therefore if not sale becomes falsy. 
------------------------------
------------------------------

10. Determine what the following code snippet prints. 
First solve it in your head or on paper, then run it in your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19

is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)

print(is_moving)

Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
------------------------------

the first print(is_moving) will print True
yeah we could have written it without parantheses, but it's not recommended
okay solution says we need the parantheses
'''


