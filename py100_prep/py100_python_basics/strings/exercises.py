'''
1. Determine the length of the string "These aren't the droids you're looking for."
- print(len("These aren't the droids you're looking for."))
------------------------------
------------------------------
2. Convert the string 'confetti floating everywhere' to all upper case.

string = 'confetti floating everywhere'
upper_string = string.upper()
print(upper_string)
------------------------------
------------------------------
3. Using the following code, 
compare the value of name with the string 'RoGeR' 
while ignoring the case of both strings. 
Print true if the values are the same; 
print false if they aren't. 
Next, perform a case-insensitive comparison 
between the value of name and the string 'DAVE'.

name = 'Roger'
string = 'RoGeR'
string2 = 'DAVE'

if name.lower() == string.lower():
    print (True)
else:
    print (False)


if name.lower() == string2.lower():
    print(True)
else:
    print(False)

- okay so it seems like I read the question wrong there
- you had the right intuition in using the str.lower() method, but this won't work in all cases

------------------------------
------------------------------
4. How can you assign the following rhyme to a single variable while preserving the line break?

A pirate I was meant to be!
Trim the sails and roam the sea!

- I think we can use tripple quotes here
rhyme = <tripple quote here>
A pirate I was meant to be!
Trim the sails and roam the sea!
<tripple quote>
------------------------------
------------------------------
5. Write code that checks whether the string char_sequence contains the character x.

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)
------------------------------
------------------------------
6. Write a function that checks whether a string is empty or not. For example:

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

def is_empty(string):
    if len(string) == 0:
        print(True)
    else:
        print(False)

is_empty(' ')

- aaah okay cool so a better way to do this would be to just directly return the result of a comparison!!

def is_empty(string):
    return string == ''

- a more Pythonic way would be to return the result of using the not operator, because an empty string is falsy
- Therefore returning the not of falsy, means True

def is_empty(string):
    return not string
------------------------------
------------------------------
7. Write an is_empty_or_blank function to determine
 whether a string is either empty or consists entirely of spaces. For example:

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

def is_empty_or_blank(s):
    if len(s) == 0 or s.isspace():
        return True
    else:
        return False


def is_empty_or_blank(s):
    return True if (len(s) == 0 or s.isspace()) else  False

def is_empty_or_blank(s):
    return s.strip(' ') == ''

print(is_empty_or_blank('rwetergt'))

def is_empty_or_blank(s):
    return not s.strip(' ')
------------------------------
------------------------------
8. Write code that capitalizes the words 
in the string 'launch school tech & talk', 
so that you get the string 'Launch School Tech & Talk'.

string = 'launch school tech & talk'

list = string.split()

for index, element in enumerate(list):
    list[index] = element.capitalize()

capitalized_string = ' '.join(list)

print(capitalized_string)
------------------------------
------------------------------
9. Write a function that checks whether a string starts with a specific prefix.

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True


def starts_with(string, prefix):
    return string.startswith(prefix)
------------------------------
------------------------------
10. Write a function that counts the number of occurrences of a substring in a string.

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

def count_substrings(string, substring):
    return string.count(substring)
'''





