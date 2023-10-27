class Account:
    def __init__(self,holder = "",amount = 0):
        self.__holder = holder
        self.__amount = amount
    
    @property
    def holder(self):
        return self.__holder
    
    @holder.setter
    def holder(self,value):
        self.__holder = value

    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self,value):
        self.__amount = value
    
    def get_money(self,money):
        if (self.__amount > 0):
            self.__amount = self.__amount - money
            print(f"Ha retirado {money}, sus fondos actuales son {self.__amount}")
        else:
            print("Saldo insuficiente")