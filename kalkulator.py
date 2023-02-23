import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

choice = int(input('''
Podaj działanie jakie chcesz wykonać, wybierając odpowiednią liczbę:
1. Dodawanie
2. Odejmowanie
3. Mnozenie
4. Dzielenie
Twój wybór: '''))

if choice < 1 or choice > 4:
    logging.error('Wybór nieprawidłowy')
    exit(1)

num1 = float(input('Podaj pierwszą wartość: '))
num2 = float(input('Podaj drugą wartość: '))

def sum(x, y):
    result = x + y
    print(f'Wynik to: {result}')

def difr(x, y):
    result = x - y
    print(f'Wynik to: {result}')

def iloczyn(x, y):
    result = x * y
    print(f'Wynik to: {result}')

def iloraz(x, y):
    result = x / y
    print(f'Wynik to: {result}')

if choice == 1:
    logging.info(f'Dodaję {num1} + {num2}')
    sum(num1, num2)
    
if choice == 2:    
    logging.info(f'Odejmuję {num1} - {num2}')
    difr(num1, num2)
    
if choice == 3:    
    logging.info(f'Mnozę {num1} * {num2}')
    iloczyn(num1, num2)

if choice == 4:    
    logging.info(f'Dzielę {num1} / {num2}')
    iloraz(num1, num2)
