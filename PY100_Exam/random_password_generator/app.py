""" Программа - генератор случайных паролей"""

import string
from random import sample, shuffle
from typing import Never


def initial_data() -> tuple[int, str]:
    """
    Функция производит валидацию введенных пользователем значений длины пароля и спецсимволов
    :return: Кортеж из: Целое число - длина пароля, Строка спецсимволов для генерации пароля
    """
    print("Добро пожаловать в программу по генерации случайных паролей!")

    while True:
        password_len = input(f"{'.' * 100}\nВведите длину желаемого пароля более 5 символов: ")
        if not password_len.isdigit():
            print("Нужно ввести только целое число!!!")
            continue

        if int(password_len) < 6:
            print("Пароль должен быть более 5 символов!!!")
            continue
        password_len = int(password_len)
        break

    set_all_spec_symbols = string.punctuation
    set_all_spec_symbols = set(set_all_spec_symbols)
    set_all_spec_symbols.add('№')
    while True:
        spec_symbols = input(f"{'*' * 100}\nВведите спецсимволы, если их нужно использовать в пароле. Иначе нажмите Ввод: ")
        spec_symbols = set(spec_symbols)

        if ' ' in spec_symbols or not spec_symbols.issubset(set_all_spec_symbols):
            print("Нужно ввести только спецсимволы без букв, цифр и пробелов!!!")
            continue

        if len(spec_symbols) > password_len:
            print("Количество спецсимволов не может быть больше длины пароля. Повторите ввод!!!")
            continue
        break

    spec_symbols = ''.join(spec_symbols)
    print("-" * 100)
    if spec_symbols:
        print(f"Будет сгенерирован пароль из '{password_len - len(spec_symbols)}' символов и спецсимволов: {spec_symbols}")
    else:
        print(f"Будет сгенерирован пароль из '{password_len}' символов")

    return password_len, spec_symbols


def generator(password_len: int = 5, spec_symbols: str = '') -> list:
    """
    Функция генерирует последовательность случайных символов из букв, цифр и спецсимволов.
    :param password_len: Длина пароля
    :param spec_symbols: Используемые спецсимволы
    :return: Последовательность случайных символов
    """

    list_symbols = sample(
        string.digits +
        string.ascii_lowercase +
        string.ascii_uppercase,
        password_len - len(spec_symbols))

    list_symbols += list(spec_symbols)
    shuffle(list_symbols)

    return list_symbols


def main() -> Never:
    """
    Главная функция генератора случайной последовательности.
    :return: Ничего не возвращает.
    """
    # password_len, spec_symbols = initial_data()
    # password = generator(password_len, spec_symbols)
    password = generator(*initial_data())

    filename = input(f"{'-' * 100}\n"
                     f"Введите имя файла для сохранения пароля или нажмите Ввод если пароль нужно только показать: ")
    if not filename:
        print(f"{'*' * 100}\nВаш сгенерированый пароль: {''.join(password)}")
    else:
        with open(filename, 'w', encoding='utf-8') as secret_file:
            secret_file.writelines(''.join(password))
        print(f"{'*' * 100}\nСоздан файл {filename} с паролем.")


if __name__ == '__main__':
    main()

