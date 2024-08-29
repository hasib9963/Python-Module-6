from abc import ABC, abstractmethod
# abtract base class
class Animal(ABC):
    @abstractmethod # enforce all derived method to have a eat method
    def eat(self):
        print('I need food')
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name 
        super().__init__()
    def eat(self):
        print('Hey nana, i am eating banana')
    def move(self):
        print("Lets move the body")

lyka = Monkey('lucky')
lyka.eat()
lyka.move()