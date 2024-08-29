class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running {self.brand} laptop.'
    
    def coding(self):
        return f'Learning and practicing python'
    
class Phone:
    def __init__(self, brand, price,color, ram,rom) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
        self.rom = rom

    def run(self):
        return f'phone tipa off kor'

    def phone_call(self, number, text):
        return f'sending sms to {number} with {text}'
    
class Camera:
    def __init__(self, brand, price, color, mega_pixel) -> None:
        self.brand = brand 
        self.price = price 
        self.color = color 
        self.mega_pixel = mega_pixel 

    def run(self):
        pass

    def change_lens(self):
        pass