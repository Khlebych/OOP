"""
Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse.
Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)

Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа).
В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде
кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или
Ellipse). Координаты также генерируются случайным образом (числовые значения).

Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""

from random import randint, choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


NUM = 7


def gen_lst():
    """ формирует список element в количестве NUM элементов """

    element = []
    lst = [Line, Rect, Ellipse]

    for i in range(NUM):
        random_class = choice(lst)
        a = randint(-1000,1000)
        b = randint(-1000, 1000)
        c = randint(-1000, 1000)
        d = randint(-1000, 1000)
        if random_class.__name__ == 'Line':
            element.append(random_class(0,0,0,0))
        else:
            element.append(random_class(a, b, c, d))

    return element


elements = gen_lst()


for el in elements:
    print(el.__class__,el.__dict__)
