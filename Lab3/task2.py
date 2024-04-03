# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sep_=','):
    common_participants = list(set(first_group.split(sep_)).intersection(second_group.split(sep_)))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print('Общие участники: ', find_common_participants(participants_first_group, participants_second_group, "|"))
