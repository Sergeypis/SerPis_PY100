# Исходные данные задачи
SIZE_DISK = 1.44 * 1024 ** 2  # размер дискеты в байтах
SIZE_CHAR = 4  # размер одного символа

page = 100  # страниц в одной книге
string_on_page = 50  # строк на одной странице
char_in_string = 25  # символов в одной строке

# TODO Найдите количество книг, которое можно разместить на дискете
size_one_book = SIZE_CHAR * char_in_string * string_on_page * page  # размер книги
count_of_books = SIZE_DISK // size_one_book

print("Количество книг, помещающихся на дискету:", int(count_of_books))
