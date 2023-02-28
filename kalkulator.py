import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def sum(x, y):
    return x + y

def difr(x, y):
    return x - y

def iloczyn(x, y):
    return x * y

def iloraz(x, y):
    return x / y

def get_data():
    choice = int(input('Twój wybór: '))
    if choice < 1 or choice > 4:
        logging.warning('Nieprawidłowy wybór')
        exit(1)
    x = float(input('Podaj pierwszą wartość: '))
    y = float(input('Podaj drugą wartość: '))

    if choice == 1:
        logging.info(f'Dodaję {x} + {y}')
        print(f'Wynik to: {sum(x, y)}')
    elif choice == 2:
        logging.info(f'Odejmuję {x} - {y}')
        print(f'Wynik to {difr(x, y)}')
    elif choice == 3:
        logging.info(f'Mnozę {x} * {y}')
        print(f'Wynik to {iloczyn(x, y)}')
    elif choice == 4:
        logging.info(f'Dzielę {x} / {y}')
        print(f'Wynik to {iloraz(x, y)}')

def calculator():
    logging.info('''
Podaj działanie, które chcesz wykonać, wybierając odpowiednią liczbę:
1. Dodawanie
2. Odejmowanie
3. Mnozenie
4. Dzielenie''')
    get_data()  

if __name__ == "__main__":
    calculator()

