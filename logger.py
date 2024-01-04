from date_create import *

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