class Triangle:
    def __init__(self,side_1 = 0,side_2 = 0,side_3 = 0):
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3
    
    @property
    def side_1(self):
        return self.__self_1
    
    @side_1.setter
    def side_1(self, value):
        self.__side_1 = value

    @property
    def side_2(self):
        return self.__self_2
    
    @side_2.setter
    def side_2(self, value):
        self.__side_2 = value
    
    @property
    def side_3(self):
        return self.__self_3
    
    @side_3.setter
    def side_3(self, value):
        self.__side_3 = value
    
    def major_side(self):
        major = max(self.__side_1, self.__side_2, self.__side_3)
        return major
    
    def type_triangle(self):
        if (self.__side_1 == self.__side_2 == self.__side_3):
            print("Es un trianglo equilatero")
        elif (self.__side_1 == self.__side_2 != self.__side_3):
            print("Es un triangulo isoceles")
        elif (self.__side_2 == self.__side_3 != self.__side_1):
            print("Es un triangulo isoceles")
        elif (self.__side_1 == self.__side_3 != self.__side_2):
            print("Es un triangulo isoceles")
        else:
            print("Es un triangulo escaleno")
            