money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget = money_capital + salary
while budget >= spend:
    budget = budget - spend + salary
    month += 1
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", month)
