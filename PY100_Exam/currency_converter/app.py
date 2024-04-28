# Your API Key: e3f0496a33a63bdd9302078b

import requests
import os
import json
from time import sleep
# from typing import Optional, Never
from typing import Optional


HELLO_TXT = 'Добро пожаловать в программу Конвертер валют'
INPUT_BASE_CURRENCY = 'Введите код исходной валюты (например, USD): '
INPUT_TARGET_CURRENCY = 'Введите код целевой валюты (например, RUB): '
FILENAME_KEY_ACCESS = 'key_access.txt'
FILENAME_CURRENCY_JSON = 'currency.json'


def read_key_access(filename: str) -> Optional[str]:
    """
    Функция проверяет наличие файла с ключем доступа к сайту обмена валюты.
    :param filename: Имя файла для проверки
    :return: Ключ доступа, строка или None.
    """
    if os.path.exists(filename):
        with open(filename) as f:
            data_key = f.read().strip()
            return None if data_key == '' else data_key

    return None


def input_key() -> str:
    """
    Функция запрашивает пользователя ввод ключа доступа к серверу.
    Производит валидацию введённых данных.
    :return: Ключ доступа API KEY, строка.
    """
    while True:
        user_key = input("Отсутствует ключ доступа к серверу. Введите ключ: ")
        if ' ' in user_key:
            print("В ведённом ключе обнаружены пробелы.Повторите ввод!!!")
            continue
        elif not user_key:
            print("Вы не ввели ключ.Повторите ввод!!!")
            continue
        break

    return user_key


def write_key_access(user_key: str, filename: str) -> bool:
    """
    Функция создаёт и записывает введённый пользователем ключ доступа в файл key_access.txt.
    :param user_key: Ключ доступа API KEY, строка.
    :param filename: Имя файла для записи.
    :return: Статус операции.
    """
    if isinstance(user_key, str) and user_key:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(user_key)
        return True
    else:
        return False


def input_currency(text_request: str, filename: str) -> Optional[str]:
    """
    Функция обработчик ввода пользователем валюты. Проверяет правильность ввода валюты в соответствии со списком.
    :param text_request: Текст запроса для вывода пользователю.
    :param filename: Имя файла со списком разрешенных ко вводу валют.
    :return: Кода валюты или None, если файл JSON не найден.
    """
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            dict_currency = json.load(f)
            list_currency = [curr["код"] for curr in dict_currency["валюты"]]
            while True:
                currency = input(text_request).upper()
                if currency in list_currency:
                    return currency
                else:
                    print("Такого кода нет. Выберете код валюты из списка и повторите ввод: ")
                    print("-" * 6 * len(list_currency) + "-")
                    for i in list_currency:
                        print(f"|{i:^5}", end='')
                    print("|")
                    print("-" * 6 * len(list_currency) + "-")
                    continue
    print(f"{'!' * 3}\nОшибка!!! Не найден файл currency.json")
    return None


def currency_converter(base_currency: str, target_currency: str, key: str) -> None:
    """
    Функция производит запрос на сервере https://v6.exchangerate-api.com курса конвертации валют для базовой валюты
    полученной от пользователя. Производит расчет целевой валюты на основании введенной пользователем суммы.
    :param base_currency: Базовая валюта в формате кода из 3х букв, например: 'USD'
    :param target_currency: Целевая валюта в формате кода из 3х букв, например: 'RUB'
    :param key: Ключ доступа API KEY
    :return: Ничего не возвращает.
    """
    while True:
        amount = input("Введите сумму для конвертации: ")
        try:
            amount = float(amount)
            if amount < 0:
                print(f"Ошибка!!! Введёное число должно быть положительным. Повторите ввод...")
                continue
        except ValueError:
            print(f"Вы ввели недопустимое значение: '{amount}'. Повторите ввод...")
            continue
        else:
            break

    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{base_currency}"

    count_conn = 0
    while count_conn != 3:
        try:
            response = requests.get(url)
            if not response.ok:
                print(f"{'!' * 3}\nОшибка сервера. Что-то пошло не так. Повторите запрос позже.")
                exit()
            data = response.json()
            conversion_rate = data.get('conversion_rates').get(target_currency)
            result_convertation = conversion_rate * amount

            print(f"{'=' * 48}\n"
                  f"За {amount:.2f} {base_currency} получите {result_convertation:.2f} {target_currency}\n"
                  f"{'=' * 48}"
                  )
            break
        except OSError:
            print("\nОшибка соединения с сервером. Повторная попытка через:")
            for count_time in range(5, 0, -1):
                print(f"{count_time}..", end='')
                sleep(1)
            count_conn += 1
            continue
    else:
        print(f"\n{'-' * 55}\nНет связи с сервером обмена валюты. Программа завершена.")
        exit()


def main():
    """
    Главная функция программы конвертера валют.
    :return: Ничего не возвращает.
    """
    print("*" * (len(HELLO_TXT) + 4))
    print(f"* {HELLO_TXT} *")
    print("*" * (len(HELLO_TXT) + 4))

    key = read_key_access(FILENAME_KEY_ACCESS)
    if key is None:
        key = input_key()
        if write_key_access(key, FILENAME_KEY_ACCESS):
            print("Ваш ключ успешно сохранён в файле key_access.txt")
        else:
            print("Непредвиденная ошибка. Ключ не сохранён. Обратитесь к разработчику.")

    base_currency = input_currency(INPUT_BASE_CURRENCY, FILENAME_CURRENCY_JSON)
    target_currency = input_currency(INPUT_TARGET_CURRENCY, FILENAME_CURRENCY_JSON)
    if base_currency is None or target_currency is None:
        exit()

    currency_converter(base_currency, target_currency, key)


if __name__ == '__main__':
    main()
