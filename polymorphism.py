# poly --> many (multiple)
# morph --> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name 

    def make_sound(self):
        print("animal make some sound")

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('ghew ghew')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('maah maah maah')

don = Cat('Real don SRK')
don.make_sound()

shepard = Dog('German Shepard')
shepard.make_sound()

ram = Goat('Ram chagol')
ram.make_sound()

less = Goat('gora gori khay')

animals = [don, shepard, ram, less]
for animal in animals:
    animal.make_sound()