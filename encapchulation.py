# encapsulation --> hide details
# access modifier: public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holeder_name = holder_name # public attribute
        self._branch = 'Banani 11' # protected attribute
        self.__balance = initial_deposit # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
         self.__balance = self.__balance - amount
         return   amount 
        else:
            return f'fokira taka nai'

rafsan = Bank('small bro', 1200)
print(rafsan.holeder_name)
rafsan.holeder_name = 'Boro vai'
# print(rafsan.balance)
rafsan.deposit(7000)
print(rafsan.get_balance())
print(rafsan.holeder_name)
print(rafsan._branch)
# print(dir(rafsan))
print(rafsan._Bank__balance)