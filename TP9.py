from Persona import Person
from Cuenta import Account
from Triangulo import Triangle
from Agenda import Diary

# Exercise 1
person_1 = Person(44771675,"Valentin",18)
person_2 = Person(36125987,"Juan",20)
person_3 = Person(41236471,"Carlos",30)

print("Datos: ")
person_1.show()
person_2.show()
person_3.show()

print(f"¿{person_1.name} es mayor de edad? {person_1.major()}")
print(f"¿{person_2.name} es mayor de edad? {person_2.major()}")
print(f"¿{person_3.name} es mayor de edad? {person_3.major()}")

# Exercise 2
acc1 = Account()

while True:
    name = input("Ingrese su nombre: ")
    if (name == ""):
        print("Nombre incorrecto")
    else:
        acc1.holder = name
        break

while True:
    print("1. Ingresar dinero")
    print("2. Sacar dinero")
    print("3. Ver dinero")
    print("4. Salir")
    choice = input("Ingrese su opcion: ")
    if choice == "1":
        acc1.amount = float(input("Ingrese la cantidad de plata: "))
    elif choice == "2":
        withdraw = float(input("Ingrese el dinero a sacar: "))
        acc1.get_money(withdraw)
    elif choice == "3":
        print(f"Tienes ${acc1.amount}")
    elif choice == "4":
        print("Gracias por usar nuestros servicios")
        break
    else:
        print("Ingrese una opcion valida")

# Exercise 3
total_triangle = Triangle()
side_1 = float(input("Ingrese el lado 1: "))
side_2 = float(input("Ingrese el lado 2: "))
side_3 = float(input("Ingrese el lado 3: "))

total_triangle.side_1 = side_1
total_triangle.side_2 = side_2
total_triangle.side_3 = side_3

print(f"El lado mas grande del triangulo es: {total_triangle.major_side()}")
total_triangle.type_triangle()

# Exercise 4
schedule = Diary()

while True:
    print("1. Agregar contacto")
    print("2. Lista de contactos")
    print("3. Buscar contactos")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    selection = input("Ingrese su opcion: ")

    if selection == "1":
        name = input("Ingrese el nombre y apellido: ").title()
        number_phone = input("Ingrese el numero del contacto: ")
        mail = input("Ingrese el correo electronico de la persona: ").title()
        schedule.contact = name
        schedule.phone = number_phone
        schedule.email = mail
        schedule.add_contact()
    elif selection == "2":
        print(f"{schedule.view_contacts()}")
    elif selection == "3":
        key_name = input("Ingrese el dato que desea buscar: ").title()
        if schedule.search_contact(key_name) == None:
            print("No se ha encontrado el contacto")
        else:
            print("Datos del contacto: ")
            print(f"{schedule.search_contact(key_name)}")
    elif selection == "4":
        key_modify = input("Ingrese el contacto que quiere modificar: ").title()
        print(schedule.modify_contact(key_modify))
    elif selection == "5":
        print("Hasta luego!")
        break
    else:
        print("Ingrese una opcion valida")