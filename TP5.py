import Funciones
# Exercise 1
DNI = input(print("Ingrese su DNI"))
print(Funciones.validation(DNI))

# Exercise 2
word = input("Ingrese una palabra: ")
print(f"La longitud de la ultima palabra es {Funciones.lastword(word)}")

# Exercise 3
name = input("Ingrese su nombre y apellido completo: ")
name = Funciones.name(name,0)
surname = Funciones.name(name,-1)

while True:
    DNI = input("Ingrese su DNI: ")
    if Funciones.validation(DNI):
        break
    else:
        print("Ingrese un DNI valido.")

print(f"Su ID de usuario es: {Funciones.user(name,surname,DNI)}")

# Exercise 4
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

if Funciones.multiple(num_1,num_2) == True:
    print("Es multiplo")
else:
    print("No es multiplo")

# Exercise 5
days = int(input("Ingrese la cantidad de dias sobre los que quiere saber el clima: "))

for i in range(0,days):
    print(f"Dia {i+1}:")
    max = int(input("Ingrese la temperatura maxima: "))
    min = int(input("Ingrese la temperatura minima: "))
    print(f"La temperatura media es: {Funciones.average(max,min)}°C")

# Exercise 6
sentence = input("Ingrese una palabra: ").lower()
print(f"{Funciones.interspace(sentence)}")

# Exercise 7
numbers = []
while True:
    num = float(input("Ingrese un numero, presione 0 si desea terminar: "))
    if num == 0:
        break
    numbers.append(num)
print(f"El numero mas grande es: {Funciones.maxnumber(numbers)}")
print(f"El numero mas pequeño es {Funciones.minnumber(numbers)}")

# Exercise 8
radius = float(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es {Funciones.calculate_area(radius)} y su perimetro es {Funciones.calculate_perimeter(radius)}")

# Exercise 9
tries = 0
while True:
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if Funciones.login(username, password) == True:
        print("Acceso permitido")
        break
    elif Funciones.login(username,password) == False:
        print("Acceso denegado")
        tries += 1
    
    if tries == 3:
        print("Maximo de intentos alcanzados")
        break

# Exercise 10
shopping = {
    1000 : 50,
    700 : 40,
    2650 : 25,
}

print(f"La lista de compras se compone de [Precio - descuento (%)] : {shopping}")
print(f"El total de la compra con descuentos es: ${Funciones.discount(shopping)}")

# Exercise 11
list_size = int(input("Ingrese el tamaño de su lista: "))
total_list = []

for i in range(0,list_size):
    entry_list = input("Ingrese elemento de la lista: ")
    total_list.append(entry_list)

print(f"La lista invertida es {Funciones.change_list(total_list)}")

# Exercise 12
speech = input("Ingrese una frase: ")
print(f"{Funciones.dictionary_speech(speech)}")

# Exercise 13
component_x = float(input("Ingrese el valor de x: "))
component_y = float(input("Ingrese el valor de y: "))

print(f"El modulo del vector es de {Funciones.module(component_x,component_y)}")

# Exercise 14
num_3 = int(input("Ingrese un numero para saber si es primo: "))

if (Funciones.Prime_numbers(num_3)) == True:
    print(f"El numero {num_3} es primo")
else:
    print(f"El numero {num_3} no es primo")

# Exercise 15
counter = 0
while True:
    num_4 = int(input("Ingrese un numero, ingrese 0 si desea finalizar: "))
    if num_4 != 0:
        print(f"El factorial de {num_4} es {Funciones.factorial(num_4)}")
        counter += 1
    else:
        print(f"Se ingresaron {counter} numeros")
        break

# Exercise 16
num_5 = int(input("Ingrese un numero: "))
digit = int(input("Ingrese el digito que quiere saber cuantas veces aparece en el numero anterior: "))

print(f"La cantidad de veces que aparece el numero {digit} en {num_5} es {Funciones.digit_in_number(num_5,digit)}")

# Exercise 17
while True:
    prime_number = int(input("Ingrese un numero, si no es primo, el programa finalizara: "))
    if Funciones.prime_numbers(prime_number) == True:
        print("¡Ha ingresado un numero primo!")
        addition = Funciones.digits_addition(prime_number)
        print(f"La suma de los digitos del numero primo ingresado es {addition}")
        digit = int(input("Ingrese un numero para saber cuantas veces aparece en la suma anterior: "))
        print(f"La cantidad de veces que aparece el numero en la suma es: {Funciones.digit_in_number(addition,digit)}")
        maxnum = Funciones.bigger(prime_number)
    else:
        print("Ingreso un numero no primo")
        print(f"El factorial del mayor numero primo ingresado es: {Funciones.factorial(maxnum)}")
        break