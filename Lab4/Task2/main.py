# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(delimiter: str = ",", new_line: str = "\n") -> None:
    """Функция конвертер из формата CSV в формат JSON"""
    with open(INPUT_FILENAME, "r") as input_csv:
        csv_data = [line for line in csv.DictReader(input_csv, delimiter=delimiter, quotechar=new_line)]

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_json:
        json.dump(csv_data, output_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
