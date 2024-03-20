numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
total_num = len(numbers)  # количество элементов списка
none_index = numbers.index(None)  # индекс пропущенного элемента
sum_ = sum(numbers[:none_index]) + sum(numbers[none_index + 1:])  # сумма элементов кроме пропущенного
average_num = round(sum_ / total_num, 2)  # среднее арифметическое
new_numbers = numbers.copy()  # копия списка
new_numbers[none_index] = average_num

print("Измененный список:", new_numbers)
