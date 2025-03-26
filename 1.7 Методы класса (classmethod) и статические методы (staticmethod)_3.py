"""
Подвиг 8.
Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен
иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
                            если номер в верном формате и False - в противном случае.
Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).

check_name(name) - проверяет строку name с именем пользователя карты.
Возвращает булево значение True, если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и
цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

Для проверки допустимых символов в классе должен быть прописан атрибут:
CHARS_FOR_NAME = ascii_lowercase.upper() + digits

Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и
@staticmethod).
"""
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod # используем статик, т к внутри метода нет обращения к атрибутам класса
    def check_card_number(number):
        """ Формат номера : XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9) """

        if number.count('-') != 3:
            return False
        for i in number.split('-'):
            if len(i) != 4:
                return False
            for ii in i:
                if ii not in digits:
                    return False
        return True

    @classmethod # используем classmethod, т к внутри метода есть обращения к атрибутам класса
    def check_name(cls,name):
        """ Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими
        символами и цифрами. """

        if name.count(' ') != 1:
            return False
        for i in name:
            if i not in cls.CHARS_FOR_NAME + ' ':
                return False
        return True


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# print(is_number)

is_name = CardCheck.check_name('SERGEI BALAKIREV')
# print(is_name)
