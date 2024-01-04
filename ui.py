from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass

    command = '-1'
    while command != '4':
        print('возможные варианты взаимодействия: \n'
            '1. добавить контакт\n'
            '2. вывести на экран\n'
            '3. поиск контакта\n'
            '4. выход из программы')
    #print()
        command = input('введите номер действия: ')

        while command not in ('1', '2', '3', '4'):
            print('некорректные данные, нужно ввестти число команды')
            command = input('введите номер дейтсвия: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print('всего хорошего')

interface()