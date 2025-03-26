"""
Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
cart = Cart()
Каждый объект класса Cart должен иметь:
 локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup).
 Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:
    name - наименование;
    price - цена.

Создайте в программе объект cart класса Cart.
Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup).
Названия и цены придумайте сами.

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""


class Cart:
    """ корзина """

    def __init__(self):
        self.goods = []  # список объектов для покупки (объекты классов Table, TV, Notebook и Cup)

    def add(self, gd):
        """ добавление в корзину товара, представленного объектом gd """

        self.gd = gd
        self.goods.append(gd)

    def remove(self, indx):
        """- удаление из корзины товара по индексу indx """
        self.indx = indx
        del self.goods[indx]

    def get_list(self):
        """ - получение из корзины товаров в виде списка из строк:
        ['<наименовние_1>: <цена_1>','<наименовние_2>: <цена_2>',...,'<наименовние_N>: <цена_N>'] """

        return [f'{gd.name}: {gd.price}' for gd in self.goods]


class Product:

    def __init__(self, name, price):
        self.name = name  # наименование;
        self.price = price  # цена


Table = TV = Notebook = Cup = Product

tv1 = TV("TV1", "100")
tv2 = TV("TV2", "200")
table1 = Table("Table1", "10")
nout1 = Notebook("Notebook1", "1000")
nout2 = Notebook("Notebook2", "12000")
cup1 = Cup("Cup1", "5")

# Создайте в программе объект cart класса Cart
# Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup)
cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table1)
cart.add(nout1)
cart.add(nout2)
cart.add(cup1)

# print(cart.get_list())
# cart.remove(4)
# print(cart.get_list())
# cart.add(nout2)
print(cart.get_list())
