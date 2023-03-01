import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def add(x, y):
    logging.info(f'Dodaję: {x} + {y}')
    return x + y

def subtract(x, y):
    logging.info(f'Odejmuję: {x} - {y}')
    return x - y

def multiple(x, y):
    logging.info(f'Mnozę: {x} * {y}')
    return x * y

def divide(x, y):
    logging.info(f'Dzielę: {x} / {y}')
    return x / y

def get_data():
    choice = str(input('Twój wybór: '))
    if choice not in ('1,2,3,4'):
        logging.warning('Nieprawidłowy wybór')
        exit(1)
    x = int(input('Podaj pierwszą wartość:'))   
    y = int(input('Podaj drugą wartośc:'))
    return choice, x, y

operations = {
    '1': add,
    '2': subtract,
    '3': multiple,
    '4': divide
}

def calculate():
    choice, x, y = get_data()
    result = operations[choice](x, y)    
    print(f'Wynik to {result}')

if __name__ == "__main__":
    logging.info('''
Jaką operację chcesz wykonać? Podaj odpowiednią liczbę:
1. Dodawanie
2. Odejmowanie
3. Mnozenie
4. Dzielenie''')
    calculate()
