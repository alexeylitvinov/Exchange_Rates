from datetime import datetime

from utils.func import get_currency_rate, save_to_json


def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод')
            continue
        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M')
        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)
        while True:
            choice = input('Выберите действие: (1 - продолжить 2 - выйти): ')
            if choice == '1':
                break
            elif choice == '2':
                exit()
            else:
                print('Некорректный ввод')
                continue


if __name__ == '__main__':
    main()
