# Функция count_letters
def count_letters(text):
    letters = {}
    for symbol in text:
        if symbol.isalpha():
            symbol = symbol.lower()
            if symbol in letters:
                value_ = letters.get(symbol)
                letters[symbol] = value_ + 1
            else:
                letters[symbol] = 1
    return letters


# Функция calculate_frequency
def calculate_frequency(dict_):
    letters_freq = {}
    total_symbol = sum(dict_.values())
    for symbol, count_symbol in dict_.items():
        filling_symbol = count_symbol / total_symbol
        letters_freq.setdefault(symbol, filling_symbol)
    return letters_freq


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result = calculate_frequency(count_letters(main_str))
for key, value in result.items():
    print(f"{key}: {value:.2f}")
