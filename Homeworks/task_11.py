class Animals:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        return f'{self.name} jumped!'

    def run(self):
        return f'{self.name} ran!'

    def birthday(self):
        self.age += 1
        return f'Its {self.name} birthday!'


class Dog(Animals):
    def bark(self):
        return f'{self.name} barked!'


dog = Dog(name='Boris', age=12, master='Vasya')


class Cat(Animals):
    def meow(self):
        return f'{self.name} meowed!'


cat = Cat(name='Kit', age=10, master='Boris')


class Parrot(Animals):
    def fly(self):
        return f'{self.name} flew!'


parrot = Parrot(name='Semen', age=2, master='Masha')
