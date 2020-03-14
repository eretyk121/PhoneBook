
class Contact:

    def __init__(self, f_name, s_name, phone_number, pr_number=None, **kwargs):
        self.f_name = f_name
        self.s_name = s_name
        self.phone_number = phone_number
        self.priority_number = pr_number
        self.info = kwargs

    def __str__(self):
        empty_space = '          '
        msg = str()
        for key, val in self.info.items():
            msg += f'{key}: {val}\n{empty_space}'
        if self.priority_number == None:
            self.priority_number = "Нет"
        return f'Имя: {self.f_name}\n' \
               f'Фамилия: {self.s_name}\n' \
               f'Телефон: {self.phone_number}\n' \
               f'В избранных: {self.priority_number}\n' \
               f'Доп. инфо:\n{empty_space}{msg}'

Igor = Contact('Igor', 'Soldatenkov', '89803370809', None, VK='Soldatenkov121/VK', FB="Soldatenkov121/fb",
                Mail="Soldatenkov12@rambler.ru")
Liza = Contact('Liza', 'Mosyash', '89160013456', None, VK='Soldatenkov121/VK', FB="Soldatenkov121/fb",
                Mail="Soldatenkov12@rambler.ru")
Kotik = Contact('Odissey', 'Antology', '8912456789', '3-36-63', VK='Supercat/VK', FB="FluffyMister/fb")

class Phonebook:

    def __init__(self, book_name):
        self.contact_list = []
        self.book_name = book_name

    def add_contact(self, contact_inatance):
        self.contact_list.append(contact_inatance)

    def print_contacts(self):
        for contact in self.contact_list:
            print(contact)

    def find_contact(self):
        name = input('Введите имя: ')
        family = input('Введите фамилию: ')
        for contact in self.contact_list:
            if contact.f_name == name:
                if contact.s_name == family:
                    print(contact)
                else:
                    print('Нет такого контакта')
                    break

    def remove_contacts(self):
        rem_contact_number = input("Введите номер контакта для удаления: ")
        for contact in self.contact_list:
            if contact.phone_number == rem_contact_number:
                self.contact_list.remove(contact)
                print(f'Контакст {contact.f_name} удален')

    def find_priority_numbers(self):
        for contact in self.contact_list:
            if contact.priority_number != None:
                print(f'{contact.f_name}\nИзбранные номера: {contact.priority_number}')

MyBook = Phonebook('MyBook')
MyBook.add_contact(Igor)
MyBook.add_contact(Liza)
MyBook.add_contact(Kotik)
def main():
    while True:
        print(f'Спмсок доступных функций:\n'
              f'p - Вывод всех контактов \n'
              f'f - Поиск контакта по имени и фамилии\n'
              f'c - Вывод всех избрвнных номеров\n'
              f'r - Удаление контакта\n'
              f'q - Выход')
        user_input = input('Введите команду: ')
        if user_input == 'p':
            MyBook.print_contacts()
        elif user_input == 'f':
            MyBook.find_contact()
        elif user_input == 'c':
            MyBook.find_priority_numbers()
        elif user_input == 'r':
            MyBook.remove_contacts()
        elif user_input == 'q':
            break


if __name__ == '__main__':
    main()
