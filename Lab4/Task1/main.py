# TODO решите задачу
import json

INPUT_FILE = "input.json"


def task() -> float:
    """Функция возвращает сумму произведений значений словарей из файла JSON"""
    with open(INPUT_FILE, "r") as input_json:
        json_data = json.load(input_json)
        mul_list = [item["score"] * item["weight"] for item in json_data]
        return round(sum(mul_list), 3)


if __name__ == '__main__':
    print(task())
