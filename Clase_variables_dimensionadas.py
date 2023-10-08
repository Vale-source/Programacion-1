import Funciones
# Exercise 1
passengers = [("Valentin Curiel","44771675","Santiago"),("Juan Carlos","41984166","Buenos Aires"),("Julian Perez","47889651","Chaco")]
destination = [("Santiago","Chile"),("Buenos Aires", "Argentina"),("Sao Pablo","Brasil"),("Chaco","Argentina")]

while True:
    print("1. Agregar pasajero")
    print("2. Agregar ciudades")
    print("3. Verificar ciudad")
    print("4. Vuelo a la ciudad")
    print("5. Verificar pais")
    print("6. Vuelo a pais")
    print("7. Salir")
    choice = input("Elija su opcion: ")
    
    if choice == "1":
        new_passenger = Funciones.option_1()
        passengers.append(new_passenger)
        print(f"Lista actualizada: \n {passengers}")
    elif choice == "2":
        new_city = Funciones.option_2()
        destination.append(new_city)
        print(f"Lista actualizada: \n {destination}")
    elif choice == "3":
        find_DNI = input("Ingrese el DNI del pasajero a buscar: ")
        find_city = Funciones.option_3(passengers, find_DNI)
        print(find_city)
    elif choice == "4":
        city = input("Ingrese la ciudad que quiere saber cuantos pasajeros viajan: ").title()
        city_destiny = Funciones.option_4(passengers,city)
        print(city_destiny)
    elif choice == "5":
        DNI_for_country = input("Ingrese el DNI del pasajero para ver a que pais viaja: ")
        print(Funciones.option_5(passengers,DNI_for_country,destination))
    elif choice == "6":
        country = input("Ingrese el pais para saber cuantos pasajeros viajan: ").title()
        print(Funciones.option_6(passengers,country,destination))
    elif choice == "7":
        print("Gracias por usar nuestro servicio")
        break
    else:
        print("Ingrese una opcion valida")

# Exercise 2
clients = [("Valentin Curiel","28","1654.3","Av. San Martin 698"),("Pedro Herrera","14","2498","Pedro Lencina 175"),("Valentin Curiel","7","654","Av. San Martin 698")]

while True:
    print("1. Agregar compra")
    print("2. Ver direcciones")
    print("3. Ver facturas de compra")
    print("4. Salir")
    selection = input("Ingrese su opcion: ")

    if selection == "1":
        new_clients = Funciones.add_buy()
        clients.append(new_clients)
        print(f"Lista de clientes actualizada \n {clients}")
    elif selection == "2":
        print(f"Direcciones de los clientes \n {Funciones.see_directions(clients)}")
    elif selection == "3":
        print("Facturas (Nombre del cliente, fecha, monto): ")
        print(Funciones.see_salecheck(clients))
    elif selection == "4":
        break

# Exercise 3
partners_list = {
    "1" : ["Socio N°1","Amanda nuñez","17/03/2009","S"],
    "2" : ["Socio N°2","Barbara Molina","17/03/2009","S"],
    "3" : ["Socio N°3","Lautaro Campos","17/03/2009","S"],
    "4" : ["Socio N°4","Valentin Curiel","7/10/2003","N"],
    "5" : ["Socio N°5", "Rodrigo Romero","13/03/2018","N"],
}
while True:
    print("1. Cargar Informacion")
    print("2. Ver cantidad de socios")
    print("3. Verificar cuota")
    print("4. Modificar fechas")
    print("5. Eliminar socio")
    print("6. Ver todos los socios")
    print("7. Salir")
    select = input("Ingrese su opcion: ")

    if select == "1":
        Funciones.add_partner(partners_list)
    elif select == "2":
        print(f"Cantidad de socios en el club: {Funciones.total_partners(partners_list)}")
    elif select == "3":
        print(Funciones.update_dues(partners_list))
    elif select == "4": 
        Funciones.manipulate_date(partners_list)
        print("¡Fechas actualizadas!")
    elif select == "5":
        Funciones.delete_partner(partners_list)
        print("Socio eliminado de la lista")
    elif select == "6":
        print("Listado de socios: ")
        print(partners_list)