#Exercise 1
word = input("Ingrese una palabra: ")

for i in range(10):
    print(word)

#Exercise 2
age = int(input("Ingrese su edad: "))
x = 1
while x != age+1:
    print(x)
    x += 1

#Exercise 3
number = int(input("Ingrese un numero entero positivo: "))
x = 1
if number > 0:
    while x != number+1:
        if x % 2 == 1:
            if x < number:
                print(x, end=", ")
        x += 1

#Exercise 4
regressive = int(input("Ingrese un numero entero positivo: "))
z = regressive
while z <= regressive+1:
    if (z == regressive+1) or (z < regressive+1 and z > 0):
        print(z, end=", ")
    elif z == 0:
        print(z, end=".")
    z -= 1
    if z == -1:
        break

#Exercise 5
amount = float(input("Ingrese monto a invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
years = int(input("Ingrese los años que quiere dejar la inversion: "))

annual_interest = annual_interest/100
for i in range(years):
    investment = amount + (amount*annual_interest)
    amount = investment
    print(f"El monto generado en el año {i+1} es de ${investment}")

#Exercise 6
triangle_number = int(input("Ingrese el tamaño de la piramide: "))
character = "*"

for i in range(triangle_number):
    print(character)
    character += "*"

#Exercise 7
for i in range(1,11):
    print("Tabla del",i)
    for j in range(1,11):
        print(j," x ",i," = ",j*i)
    print("-----------------")

#Exercise 8
triangle = int(input("Ingrese el tamaño de la piramide: "))

for i in range(1, triangle + 1):
    for j in range(i * 2 - 1, 0, -2):
        print(j, end=' ')
    print()

#Exercise 9
password = "holamundo"

condition = False
while condition == False:
    password_1 = input("Ingrese su contraseña: ")
    password_1 = password.lower()
    if password_1 == password:
        print("Contraseña correcta")
        condition = True
    else:
        print("Contraseña incorrecta")
        condition = False

#Exercise 10
prime_number = int(input("Ingrese un numero: "))
counter = 0

for i in range(1,prime_number+1):
    if prime_number % i == 0:
        counter += 1

if counter == 2:
    print(f"{prime_number} es un numero primo")
else:
    print(f"{prime_number} no es un numero primo")

#Exercise 11
word = input("Ingrese una palabra: ")
word = list(word)
inverse_word = word[::-1]

for i in inverse_word:
    print(i)

#Exercise 12
word = input("Ingrese una palabra: ")
letter = input("Ingrese la letra que desea buscar: ")
counter_letter = 0

for i in list(word):
    if i == letter:
        counter_letter += 1
print(f"La cantidad de veces que esta la letra '{letter}' en la palabra '{word}' es {counter_letter} ")

#Exercise 13
echo = input("Ingrese una palabra: ")

while echo != "salir":
    print(echo)
    echo = input("Ingrese una palabra: ")

#Exercise 14
number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
pair = ""
uneven = ""

for i in range(number_1,number_2+1):
    if i % 2 == 0:
        pair += str(i) + ", "
    else:
        uneven += str(i) + ", "

print(f"Los numeros pares entre {number_1} y {number_2} son {pair}")
print(f"Los numeros impares entre {number_1} y {number_2} son {uneven}")

#Exercise 15
number = int(input("Ingrese un numero mayor a 0: "))
dividers = ""

if number > 0:
    for i in range(1,number+1):
        if number % i == 0:
            dividers += str(i) + ", "

print(f"Los divisores de {number} son: {dividers}")

#Exercise 16
number_range = int(input("¿Cuantos numeros desea ingresar? "))
negative_counter = 0

for i in range(number_range):
    number_i = float(input(f"Ingrese el numero {i+1}: "))
    if number_i < 0:
        negative_counter += 1

print(f"Se han ingresado {negative_counter} numeros negativos")

#Exercise 17
vowels = ["a","e","i","o","u"]
vowels_counter = ""
word = input("Ingrese una palabra: ")

for i in range(len(word)):
    for letter in word:
        if letter in vowels:
            vowels_counter += letter + " "
            vowels.remove(letter)

print(f"Las vocales que aparecen en '{word}' son: {vowels_counter}")

#Exercise 18
fibonacci = [0,1]

for i in range(9):
    """Este condicional lo coloque para que me imprima los dos primeros numeros 1 de la sucesion
    porque si no, se realizaba la suma y mostraba un solo numero 1"""
    if fibonacci[0] == 0 and fibonacci[1] == 1:
        print(fibonacci[1]) 
        addition = fibonacci[0] + fibonacci[1]
        print(addition)
        fibonacci = [fibonacci[1],addition]
    else:
        """Lo que hago es ir reemplazando los valores de la lista, si la lista inicial
        es [0,1] la posicion 0 va a pasar a ser la posicion 1, y la posicion 1 pasa a ser
        la sumatoria de los valores"""
        addition = fibonacci[0] + fibonacci[1] 
        print(addition)
        fibonacci = [fibonacci[1],addition]

#Exercise 19
moneybox = float(input("Ingrese la cantidad de dinero que quiere ahorrar en total: "))
money = 0
deposit = 0

while deposit < moneybox:
    if money >= 0:
        deposit += money
        if deposit < moneybox:
            money = float(input("Ingrese cuanto quiere depositar: "))
        elif deposit >= moneybox:
            print(f"El total de dinero en su alcancia es de: {deposit}")
    else:
        print("Ingrese un valor positivo")
        money = float(input("Ingrese cuanto quiere depositar: "))

#Exercise 20
numbers = float(input("Ingrese un numero entero: "))
numbers_addition = 0

while numbers != 0:
    if numbers % 1 == 0:
        numbers_addition += numbers
        numbers = float(input("Ingrese un numero: "))
    else:
        numbers = float(input("El numero ingresado no debe llevar decimal: "))

print(f"La sumatoria de los numeros ingresados es: {numbers_addition} ")

#Exercise 21
condition = 1
bigger = 0

while condition == 1:
    number = float(input("Ingrese un numero entero positvo: "))
    if (number % 1 == 0) and (number > 0):
        if number > bigger:
            bigger = number
    elif number == 0:
        condition = 0
    else:
        number = float(input("El numero que ingreso era negativo o llevaba coma, ingrese otro: "))

print(f"El numero mas grande que se ingreso fue el {bigger}")

#Exercise 22
condition = 0
pair_counter = 0

while condition != 1:
    number = int(input("Ingrese un numero positivo entero: "))
    digit_addition = 0
    if number == -1:
        condition = 1
    elif number % 2 == 0: #Confirmo si el numero ingresado es par
        pair_counter += 1
    while (number % 1 == 0) and (number > 0): #En este bucle confirmo si el numero es entero y positivo
        while number > 0: #Utilizo este bucle para poder ir fraccionando el numero que ingrese e irlo sumando
            digit = number % 10
            digit_addition += digit
            number //= 10
    print(f"la suma de los digitos del numero ingresado es {digit_addition}")

print(f"Se han ingresado {pair_counter} numeros pares")

#Exercise 23 and exercise 24
condition = True
amount_addition = 0

print("Ingrese 0 si desea terminar")
while condition == True:
    amount = float(input("Ingrese el precio del producto: "))
    if amount > 0:
        amount_addition += amount
        print(amount_addition)
    elif amount == 0:
        condition = False
    else:
        amount = float(input("Ingrese un numero positivo: "))

print(f"El total a pagar es de ${amount_addition}")
if amount_addition > 1000:
    amount_addition = amount_addition - (amount_addition*0.1)
    print(f"Su compra supera los $1000, se le aplicara un descuento del 10%, el total es de ${amount_addition}")

#Exercise 25
number = int(input("Ingrese un numero: "))
factorial = 1

for i in range(1,number+1):
    factorial *= i
print(f"El factorial de {number} es: {factorial}")
