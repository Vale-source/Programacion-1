class Person:
    def __init__(self,DNI,name,age):
        self.__DNI = DNI
        self.__name = name
        self.__age = age

    @property
    def DNI(self):
        return self.__DNI
    
    @DNI.setter
    def DNI(self,value):
        self.__DNI = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    
    def show(self):
        print(f"{self.__DNI}, {self.__name}, {self.__age}")
    
    def major(self):
        if (self.__age >= 18):
            return True
        else:
            return False