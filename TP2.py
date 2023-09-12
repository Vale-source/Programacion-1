#Ejercicio 1 y Ejercicio 2
años_pc = 4
if años_pc <= 2 and años_pc > 0 :
    print("La computadora es nueva")
elif años_pc <= 0 :
    print("Error")
else:
    print("La computadora es vieja")

#Ejercicio 3
nombre_1 = input("Ingrese un nombre: ")
nombre_2 = input("Ingrese otro nombre: ")

nombre_1 = nombre_1.lower()
nombre_2 = nombre_2.lower()

nombre_1 = list(nombre_1)
nombre_2 = list(nombre_2)

if (nombre_1[0]) == (nombre_2[0]) :
    print("Coincidencia")
else:
    print("No hay concidencia")

#Ejercicio 4
candidatos = ["Candidato A","Candidato B","Candidato C"]
opc = input("Eliga un candidato (Candidato A; Candidato B; Candidato C): ")
opc = opc.title()

if opc == candidatos[0] :
    print("Usted ha votado al partido rojo")
elif opc == candidatos[1] :
    print("Usted ha votado al partido verdad")
elif opc == candidatos[2] :
    print("Usted ha votado al partido azul")
else:
    print("Opcion erronea")

#Ejercicio 5
vocales = ("a","e","i","o","u")
x = input("Ingrese una vocal: ")

if len(x) == 1 :
    if x in vocales :
        print("Es vocal")
    else:
        print("No es vocal")

else :
    print("No se puede procesar el dato")

#Ejercicio 6
año = int(input("Ingrese el año que desea conocer si es biciesto o no: "))

if año%4 == 0 :

    if año%100 != 0:
        print("Es año biciesto")
    elif año%100 == 0 and año%400 == 0:
        print("Es año biciesto")

else:
    print("No es año biciesto")

#Ejercicio 7
num_a = float(input("Ingrese el primer numero: "))
num_b = float(input("Ingrese el segundo numero: "))
num_c = float(input("Ingrese el tercer numero: "))

if (num_a < num_b) and (num_a < num_c):
    menor = num_a
elif (num_b < num_a) and (num_b < num_c):
    menor = num_b
elif (num_c < num_a) and (num_c < num_b):
    menor = num_c

print(f"El numero mas chico es {menor}")

#Ejercicio 8
ingreso = {"usuario": "Gwenevere", "contraseña" : "excalibur" }
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if (usuario == ingreso["usuario"]) and (contraseña == ingreso["contraseña"]) :
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso Denegado")

#Ejercicio 9
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo: ")

sexo = sexo .lower()
nombre = nombre .upper()
nombre = list(nombre)

if (sexo == "hombre") :
    if nombre[0] > "N":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")

elif (sexo == "mujer"):
    if nombre[0] < "M":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")

#Ejercicio 10
edad = int(input("Ingrese su edad "))

if (edad < 4) and (edad > 0) :
    print("Precio de la entrada: Gratis")
elif (edad >= 4) and (edad <= 18):
    print("Precio de la entrada: $500")
elif (edad > 18):
    print("Precio de la entrada $1000")
else:
    print("Ingrese una edad valida")

#Ejercicio 11
vegetariano = ["pimiento","tofu"]
no_vegetariano = ["peperoni","salmon","jamon"]

pizza = input("¿Desea una pizza vegetariana? ")
pizza = pizza.title()

if (pizza == "Si"):
    ingrediente = input("Elija un ingrediente para la pizza (Pimiento o Tofu): ")
    ingrediente = ingrediente.lower()
    if ingrediente in vegetariano:
        print(f"La pizza que eligio es vegetariana. Sus ingredientes son: muzzarela, tomate y {ingrediente}")
    else:
        print("Ese ingrediento no se encuentra en la lista")
elif (pizza == "No"):
    ingrediente = input("Elija un ingrediente para la pizza (Peperoni, Salmon, Jamon): ")
    ingrediente = ingrediente.lower()
    if ingrediente in no_vegetariano:
        print(f"La pizza que eligio no es vegetariana. Sus ingredientes son: muzzarela, tomate y {ingrediente}")
    else:
        print("Ese ingrediento no se encuentra en la lista")
else:
    print("Ingrese una respuesta valida")

#Ejercicio 12
año_actual = int(input("Ingrese el año actual: "))
año_x = int(input("Ingrese un año cualquiera: "))

if año_actual > año_x:
    print("Han pasado",año_actual-año_x,"años")
elif año_x > año_actual:
    print("Faltan",año_x-año_actual,"años")
else:
    print("Ingrese un año valido")

#Ejercicio 13
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

if (num_1 < 0) and (num_2 < 0):
    if num_1 > num_2:
        if num_1%num_2 == 0:
            print(f"El numero {num_1} es multiplo de {num_2}")
        else:
            print(f"El numero {num_1} no es multiplo de {num_2}")
    elif num_2 > num_1:
        if num_2%num_1 == 0:
            print(f"El numero {num_2} es multiplo de {num_1}")
        else:
            print(f"El numero {num_2} no es multiplo de {num_1}")
else:
    print("Ingrese un numero valido")

#Ejercicio 14
print("La formula de la ecuacion a resolver es: a*x + b = 0")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

if a != 0 :
    x = -b/a
    print(f"el valor de x es {x}")
elif (a == 0) and (b != 0) : 
    print("No hay ningun valor de x que satisfaga la ecuacion")
elif (a == 0) and (b == 0) :
    print("La ecuacion es una identidad, por ende tiene infinitas ecuaciones")

#Ejercicio 15
r = input("Desea calcular el area? (T/t para triangulo, C/c para circulo): ")

if (r == "t") or (r == "T") :
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    if (base and altura) > 0:
        area = (base*altura)/2
        print(f"El area del triangulo es: {area}")
    else:
        print("Ninguno de los valores puede ser 0")

elif (r == "c") or (r == "C") :
    radio = float(input("Ingrese el radio del circulo: "))
    if radio > 0:
        area = round(3.1415 * (radio**2),4)
        print(f"El area del circulo es: {area}")
    else:
        print("El radio debe ser mayor a 0")

else:
    print("Ingrese un valor correcto")

#Ejercicio 16
v_1 = float(input("Ingrese el primer numero: "))
v_2 = float(input("Ingrese el segundo numero: "))

operacion = int(input("1 para sumar, 2 para multiplicar, 3 para restar, 4 para dividir: "))
if operacion == 1:
    suma = v_1 + v_2
    print(f"La suma {v_1} mas {v_2} es {suma}")
elif operacion == 2 :
    mult = v_1 * v_2
    print(f"El producto de {v_1} por {v_2} es {mult}")
elif operacion == 3 :
    resta = v_1 - v_2
    print(f"La resta de {v_1} menos {v_2} es {resta}")
elif operacion == 4 :
    if v_2 != 0 :
        div = v_1/v_2
        print(f"La division de {v_1} divido {v_2} es {div}")
    else:
        print("No se puede dividir por cero")

#Ejercicio 17
semana = ["lunes","viernes","sabado","domingo"]

dia = input("Ingrese un dia de la semana: ")
dia = dia.lower()

if dia == semana[0]:
    print("Hoy es lunes")
elif dia == semana[1]:
    print("Hoy es viernes")
elif dia == semana[2] or dia == semana[3]:
    print("Estamos en fin de semana")
else:
    print("Ingrese otro valor")

#Ejercicio 18
horas = float(input("Ingrese las horas trabajadas en el mes: "))
salario = float(input("Ingrese su salario por hora: "))

salario_comun = horas*salario

if (horas > 48):
    horas_extras = horas-48
    salario_extra = horas_extras*(salario + salario*0.1)
    total = salario_extra + salario_comun
    print(f"Usted ha ganado: {total}")

elif (horas <= 48):
    print(f"Usted ha ganado: {salario_comun}")

#Ejercicio 19
lapices = int(input("Ingrese cuantos lapices compro: "))
precio = 60

if lapices >= 1000:
    total = (lapices*precio) - (lapices*precio*0.07)
    print(f"El total a pagar es de $ {total}")
elif (lapices < 1000) and (lapices > 0) :
    total = lapices*precio
    print(f"El total a pagar es de $ {total}")
else:
    print("Ingrese una cantidad valida")

#Ejercicio 20
nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))
nota_4 = float(input("Ingrese la cuarta nota: "))

nota_prom = (nota_1 + nota_2 + nota_3 + nota_4)/4
nota_prom = round(nota_prom,2)
if nota_prom >= 6:
    print(f"Aprobo con promedio de {nota_prom}")
else:
    print(f"Desaprobo con promedio de {nota_prom}")