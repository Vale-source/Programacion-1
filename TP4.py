#Exercise 0
value_x = 0

while value_x <= 30:
    value_x += 1
    if value_x == 4 or value_x == 6 or value_x == 10:
        print(f"Se salto el valor de {value_x}")
    elif value_x == 15:
        print(f"Se rompio la ejecucion del bucle cuando x valia {value_x}")
        break
    else:
        print(f"El valor del loop es {value_x}")

#Exercise 1
text_line = input("Ingrese linea: ").upper()
print(text_line)

while text_line != "":
    text_line = input("Ingrese linea: ").upper()
    print(text_line)

#Exercise 2
condition = True
money = []
total = 0

while condition == True:
    money = input("Ingrese su operacion R o D ").upper()
    if money == "":
        break
    elif money[0] == "R":
        total -= float(money[money.find(" "):])
        print(total)
    elif money[0] == "D":
        total += float(money[money.find(" "):])
print(" ")
print(total)

#Exercise 3
condition = True
prime_list = ""

while condition == True:
    number = int(input("Ingrese un numero: "))
    prime_counter = 1
    if number > 1:
        for i in range(1,number+1):
            if number % i == 0:
                prime_counter += 1
        if prime_counter == 3:
            prime_list = prime_list + str(number)
    elif number == 0:
        break

prime_list = list(prime_list)
print(f"Los numeros primos ingresados son {prime_list}")

#Exercise 4 (Lo hice con bucle for porque no sabia con cual de los dos bucles nos pedia)
"""year_1 = int(input("Ingrese un año: "))
year_2 = int(input("Ingrese otro año: "))

if year_1 < year_2:
    for i in range(year_1,year_2,1):
        if (i % 4 == 0 and i % 100 != 0):
            if i % 10 == 0:
                print(i)
        elif (i % 4 == 0 and i % 100 == 0 and i % 400 == 0):
            if i % 10 == 0:
                print(i)
elif year_2 < year_1:
    for i in range(year_2,year_1,1):
        if (i % 4 == 0 and i % 100 != 0):
            if i % 10 == 0:
                print(i)
        elif (i % 4 == 0 and i % 100 == 0 and i % 100 == 0):
            if i % 10 == 0:
                print(i)"""

year_1 = int(input("Ingrese un año: "))
year_2 = int(input("Ingrese otro año: "))


while year_1 <= year_2:
    if (year_1 % 4 == 0 and year_1 % 100 != 0) or (year_1 % 400 == 0):
        if year_1 % 10 == 0:
            print(year_1)
    year_1 +=1

while year_2 <= year_1:
    if (year_2 % 4 == 0 and year_2 % 100 != 0) or (year_2 % 400 == 0):
        if year_2 % 10 == 0:
            print(year_2)
    year_2 += 1

#Exercise 5
for i in range(1,21):
    if i % 2 == 1:
        continue
    print(i)

#Exercise 6
import random
list_size = int(input("Ingrese el rango de la lista: "))
list_to_complete= []
for i in range(0,list_size-1):
    list_to_complete.append(random.randint(0,10))

search_number = int(input("Ingrese el numero que desea encontrar: "))
for j in list_to_complete:
    if j == search_number:
        print(f"el numero {search_number} fue encontrado")
        break
    else:
        print("numero no encontrado")

#Exercise 7
condition = True

while condition == True:
    selection = int(input("Ingrese una opcion del menu (1,2,3) o ingrese 0 para salir: "))
    if selection == 1:
        print("Usted ha seleccionado la opcion 1")
        condition = True
    elif selection == 2:
        print("Usted ha seleccionad la opcion 2")
        condition = True
    elif selection == 3:
        print("Usted ha seleccionado la opcion 3")
        condition = True
    elif selection == 0:
        print("Ha seleccionado la opcion 0, el programa terminara")
        break
