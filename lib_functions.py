import json

DATA = 'data.json'

class Book:
    def __init__(self,
                 title: str,
                 author: str,
                 year: str,
                 loaded_data: list,
                 status: str ='В наличии'
                 ) -> None:

        self.id = self.generate_id(loaded_data)
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def generate_id(self, loaded_data) -> str:
        return str(max(int(item['id']) for item in loaded_data) + 1 if loaded_data else 1)



def show_lib():
    """показывает все книги из библиотеки"""
    with open(DATA, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    print()
    for book in loaded_data:
        print(f'№ {book["id"]}, '
              f'название: {book["title"]}, '
              f'автор: {book["author"]}, '
              f'год: {book["year"]}, '
              f'статус: {book["status"]}.' , sep='\n')


def search_book():
    """поиск книг по одному из фильтров"""
    with open(DATA, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)

    print('\nФильтры: номер, название, автор, год, статус(В наличии / Выдан)')
    choice = input('Введите фильтр поиска: ').lower()
    search = input('Поиск: ')


    if choice == 'номер':
        result = [item for item in loaded_data if item['id'] == search]
    elif choice == 'название':
        result = [item for item in loaded_data if item['title'] == search.capitalize()]
    elif choice == 'автор':
        result = [item for item in loaded_data if item['author'] == search.title()]
    elif choice == 'год':
        result = [item for item in loaded_data if item['year'] == search]
    elif choice == 'статус':
        result = [item for item in loaded_data if item['status'] == search.capitalize()]

    try:
        if result:
            print()
            for book in result:
                print(
                    f'№ {book["id"]}, '
                    f'название: {book["title"]}, '
                    f'автор: {book["author"]}, '
                    f'год: {book["year"]}, '
                    f'статус: {book["status"]}.',
                    sep='\n')
        else:
            print('\nПо запросу поиска ничего не найдено')
    except UnboundLocalError:
        print('\nОШИБКА ВВОДА. Попробуйте еще раз')


def book_status():
    """изменяет статус книги с "В наличии" на "Выдана" или наоборот"""
    with open(DATA, 'r+', encoding='utf-8') as file:
        loaded_data = json.load(file)
        file.seek(0)
        book_id = str(input('\nВведите номер книги: '))
        result = [item for item in loaded_data if item['id'] == book_id]

        if result:
            if result[0]['status'] == 'В наличии':
                result[0]['status'] = 'Выдан'
                print(f'\nКнига № {book_id} успешно выдана, статус изменен.')
            elif result[0]['status'] == 'Выдан':
                result[0]['status'] = 'В наличии'
                print(f'\nКнига № {book_id} возвращена, статус изменен.')
            json.dump(loaded_data, file, ensure_ascii=False, indent=4)
            file.truncate()
        else:
            print('\nКнига не найдена')


def add_book():
    """добавление новой книги в библиотеку"""
    title = input("Введите название книги: ").capitalize()
    author = input("Введите имя автора: ").title()
    year = input("Введите год выпуска: ")
    with open(DATA, 'r+', encoding='utf-8') as file:
        try:
            loaded_data = json.load(file)
            file.seek(0)
        except json.JSONDecodeError:
            loaded_data = []

        new_book = Book(title, author, year, loaded_data)


        if title and author and year:
            loaded_data.append(new_book)
            file.seek(0)
            json.dump(loaded_data, file, ensure_ascii=False, indent=4)
            print(f'\nКнига №{new_book.id} "{title}" Автор: {author} год: {year} успешно добавлена!')
        else:
            print('\nОШИБКА ВВОДА. Не все поля заполнены')


def remove_book():
    """удаляет книгу из библиотеки"""
    with open(DATA, 'r+', encoding='utf-8') as file:
        loaded_data = json.load(file)
        file.seek(0)
        book_id = str(input('\nВведите номер книги: '))
        loaded_data = [item for item in loaded_data if item['id'] != book_id]
        if loaded_data and book_id:
            print(f'\nКнига № {book_id} успешно удалена.')
            json.dump(loaded_data, file, ensure_ascii=False, indent=4)
            file.truncate()
        else:
            print('\nКнига не найдена')
