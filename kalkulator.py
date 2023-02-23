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
    print('Wybór nieprawidłowy')
    exit(1)

num1 = float(input('Podaj pierwszą wartość: '))
num2 = float(input('Podaj drugą wartość: '))

if choice == 1:
    sum = num1 + num2
    logging.info(f'Dodaję {num1} + {num2}')
    print(f'Wynik to: {sum}')

if choice == 2:
    difr = num1 - num2
    logging.info(f'Odejmuję {num1} - {num2}')
    print(f'Wynik to: {difr}')

if choice == 3:
    iloczyn = num1 * num2
    logging.info(f'Mnozę {num1} * {num2}')
    print(f'Wynik to: {iloczyn}')

if choice == 4:
    iloraz = num1 / num2
    logging.info(f'Dzielę {num1} / {num2}')
    print(f'Wynik to: {iloraz}')

logging.info('Koniec')
