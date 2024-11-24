from lib_functions import  show_lib, search_book, book_status, add_book, remove_book


def main() -> None:
    while True:
        print('\n Меню ConsoleLibrary:')
        print('[1] - Посмотреть Библиотеку')
        print('[2] - Найти книгу')
        print('[3] - Выдача книг (изменение статуса)')
        print('[4] - Добавить книгу')
        print('[5] - Удалить книгу')
        print('[6] - Выход')

        choice = input("Введите номер пункта: ")
        choices = { '1': show_lib,
                    '2': search_book,
                    '3': book_status,
                    '4': add_book,
                    '5': remove_book,
                    }

        if choice in choices:
            choices[choice]()
        elif choice == '6':
            print("Завершение работы программы.")
            break
        else:
            print('\nОШИБКА ВВОДА. Введите номер пункта.')


if __name__ == "__main__":
    main()