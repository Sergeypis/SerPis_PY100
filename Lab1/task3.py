list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_players_in_list = len(list_players)
one_team = list_players[:total_players_in_list // 2]
second_team = list_players[total_players_in_list // 2:]

print(one_team)
print(second_team)
