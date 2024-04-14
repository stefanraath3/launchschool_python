# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal

def prompt(message):
    print(f'=> {message}')


def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')
prompt("What's your first number?")
number1 = input()


while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

# Ask the user for the second number
prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

print(f'{number1} {number2}')

# Ask the user for an operation to perform
prompt('''What operation would you like to perform?
\n1) Add 2) Subtract 3) Multiply 4) Divide''')
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

# Perform the operation on the two numbers
match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)
# Print the result to the terminal

print(f"The result is: {output}")