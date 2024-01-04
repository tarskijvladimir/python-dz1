#  1) создать телефонный справочник:
#     - открыть файл в режиме (а - добавления)
#  2) добавить контакт:
#     - запросить информацию у пользователя
#     - подготовить данные в нужном формате
#     - открыть файл в режиме добавления (а)
#     - добавить контакт в файл
#  3) вывести данные из файла на экран
#     - открыть файл в режиме чтения (r)
#     - вывести информацию на экран
#  4) поиск данных:
#     - запросить вариант поиска
#     - запросить данные поиска
#     - открыть файл в режиме чтения (r)
#     - сохранить данные в переменную
#     -осуществить поиск по файлу
#     - вывести нужную информацию на экран
#  5) реализовать UI:
#     - вывести варианты меню
#     - получение запроса пользователя
#     - реализация запроса пользователя
#     - выход из программы
def input_name():
    return input('введите имя: ')
def input_surname():
    return input('введите фамилию: ')
def input_patronymic():
    return input('введите отчество: ')
def input_phone():
    return input('введите номер телефона: ')
def input_address():
    return input('введите адрес: ')

def create_contact():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{name} {surname} {patronymic} {phone}\n{address}\n\n'



def add_contact(contact):
    #contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8')as file:
        file.write(contact)

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read().rstrip())

def search_contact():
    print(
        'возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру телефона\n'
        '5. по адресу\n'
    )
    var_search = input('выберите вариант поиска: ')
                       
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('некорректные данные, нужно ввестти число команды')
            var_search = input('введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    #print(contacts_list)

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        #print(contact_lst)
        if search in contact_lst[index_var]:
            print(contact_str)


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

import shutil

def copy_file(source_file, destination_file):
    shutil.copyfile(source_file, destination_file)
