class Motorbike:
    status = "new"
    engine = False
    def __init__(self,color="red",registration="ASD123",fuel=50,wheels=2,brand="Hundai",model="RTX 3060",fabrication="19/05/2022",velocity=500,weight=324):
        self.color = color
        self.registration = registration
        self.fuel = fuel
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.fabrication = fabrication
        self.velocity = velocity
        self.weight = weight
    
    def start(self):
        if self.engine == False:
            self.engine = True
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba arrancado")
    
    def stop(self):
        if self.engine == True:
            self.engine = False
            print("El motor ha parado")
        else:
            print("El motor ya estaba frenado")
    
    def printprice(self):
        try:
            self.price = price
        except NameError:
            print("La moto no tiene precio")
        else:
            print(f"El precio de la motocicleta marca {self.brand}, modelo {self.model} es {self.price}")