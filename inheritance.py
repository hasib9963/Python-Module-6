# based class / parent class / common attributes + functinality class
# derivided class / child class / uncommon attributes + functinality class

class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running {self.brand} laptop.'


class Laptop:
    def __init__(self,memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'Learning and practicing python'
    
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, duel_sim) -> None:
        self.duel_sim = duel_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f'sending sms to {number} with {text}'
    
    def __repr__(self) -> str:
        return f'phone : {self.brand} {self.price} {self.color} {self.duel_sim}'
    
class Camera:
    def __init__(self,mega_pixel) -> None:
        self.mega_pixel = mega_pixel 

    def change_lens(self):
        pass

    # inheritance
my_phone =  Phone('iphone', 125000, 'Grey', 'USA', 'single sim')
# my_phone.phone_call()
# my_phone.color()
print(my_phone)



