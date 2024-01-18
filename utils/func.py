import json
import os

import requests

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
CURRENCY_RATE_FILE = 'currency_rate.json'


# print(os.environ['EXCHANGE_RATE_API_KEY'])
# value = os.getenv('EXCHANGE_RATE_API_KEY')
# print(value)
# print(os.environ.get('EXCHANGE_RATE_API_KEY'))
# response = requests.get('https://api.github.com')
# print(response)
# print(dir(response))
# print(response.status_code)
# print(response.content)
# print(response.text)
# j = response.json()
# print(j)
# print(type(j))
# print(j['current_user_url'])


def get_currency_rate(base: str) -> float:
    """
    Получает курс валюты относительно рубля от API и возвращает float
    :param base: str
    :return: float
    """
    url = 'https://api.apilayer.com/exchangerates_data/latest'
    response = requests.get(url, headers={"apikey": API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    """
    Сохраняет в .json файл данные приложения
    :param data: dict
    :return: None
    """
    with open(CURRENCY_RATE_FILE, 'a') as file1:
        if os.stat(CURRENCY_RATE_FILE).st_size == 0:
            json.dump([data], file1)
        else:
            with open(CURRENCY_RATE_FILE) as file2:
                data_list = json.load(file2)
                data_list.append(data)
            with open(CURRENCY_RATE_FILE, 'w') as file3:
                json.dump(data_list, file3)
