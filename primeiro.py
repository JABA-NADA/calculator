from time import sleep

print('Welcome to your personal calculator!')
sleep(0.3)

name = input('What is your name please master?:')
sleep(0.3)

print(f'Welcome to your calculator {name}!')
sleep(0.3)

while True:

    operator = input(f'What kind of operator will you use {name}? ( + , - , * , / , ):')
    sleep(0.3)

    while len(operator) != 1 or operator not in '+-*/':
        print(f'ERROR {operator} is NOT valid')
        operator = input(f'What kind of operator will you use {name}? ( + , - , * , / , ):')

    num1 = float(input(f'Tipe the 1st number:'))
    sleep(0.3)

    num2 = float(input(f'Tipe the 2nd number:'))
    sleep(0.3)

    if operator == '+':
        print(f'The result is = {num1 + num2}')

    elif operator == '-':
        print(f'The result is = {num1 - num2}')

    elif operator == '*':
        print(f'The result is = {num1 * num2}')

    elif operator == '/':
        print(f'The result is = {num1 / num2}')

    else:
        print(f'ERROR {operator} is NOT valid')

    question = input(str('Would you like to continue? [S/N]:')).upper()

    if question == 'N':
        print('The end')
        break