class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, roll, level) -> None:
        self.roll = roll
        self.level = level

class Sports:
    def __init__(self, game) -> None:
        self.game = game 

class Student(Family, School, Sports):
    def __init__(self, address, roll, level, game) -> None:
        School.__init__(self, roll, level)
        Sports.__init__(self, game)
        Family.__init__(self, address)