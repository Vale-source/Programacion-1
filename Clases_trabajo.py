from Motocicleta import Motorbike

motorbike_1 = Motorbike(fuel=10,wheels=2)
motorbike_1.start()
motorbike_1.stop()
motorbike_1.price = 1580
motorbike_1.printprice()


motorbike_2 = Motorbike()
motorbike_1.start()
motorbike_1.start()
motorbike_1.stop()
motorbike_1.stop()
motorbike_2.printprice() #Tira error porque no tiene un precio definido