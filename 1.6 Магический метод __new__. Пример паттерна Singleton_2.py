"""
Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны
быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно.
"""


class SingletonFive:
    __instance = []

    def __new__(cls, *args, **kwargs):
        while len(cls.__instance) < 4:
            new_ob = super().__new__(cls)
            cls.__instance.append(new_ob)
            return new_ob
        return cls.__instance[-1]

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]


a = SingletonFive('Первый')
print(a.__dict__, id(a))
b = SingletonFive('Второй')
print(b.__dict__, id(b))
c = SingletonFive('Третий')
print(c.__dict__, id(c))
d = SingletonFive('Четвертый')
print(d.__dict__, id(d))
e = SingletonFive('Пятый')
print(e.__dict__, id(e))
f = SingletonFive('шестой')
print(f.__dict__, id(f))
z = SingletonFive('седьмой')
print(z.__dict__, id(z))
