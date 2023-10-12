import Funciones
import random
# Exercise 1 - 2 - 3 - 4
list_num = []
while True:
    num = int(input("Ingrese un numero, pulse 0 para salir: "))

    if num == 0:

        print(f"Lista de numeros guardados: {list_num}")

        print(f"La suma de todos los numeros en la lista es {sum(list_num)}")

        new_list = []
        new_num = int(input("Ingrese otro numero para crear una nueva lista: "))
        for numinlist in list_num:
            if numinlist < new_num:
                new_list.append(numinlist)

        new_list.sort()
        print("Lista de nuevos numeros:")
        for shownum in range(len(new_list)):
            print(new_list[shownum])
            

        break

    elif num in list_num:
        index = list_num.index(num)
        del list_num[index]
        list_num.append(num)

    else:
        print(f"El número {num} no está en la lista. No se puede borrar.")
        list_num.append(num)

# Exercise 5
ocurrences_list = [5,16,2,5,57,5,2]
print(f"Lista: {ocurrences_list}")
print(f"Lista con la cantidad de aparicion de cada numero {Funciones.ocurrences(ocurrences_list)}")

# Exercise 6
primary_list = []
highschool_list = []

print("Ingrese la lista de alumnos del primario: ")
Funciones.fill_list(primary_list)
print("Ingrese la lista de alumnos del secundario: ")
Funciones.fill_list(highschool_list)

print(f"Lista de alumnos del primario (sin repetir nombres): {Funciones.printlist(primary_list)}")
print(f"Lista de alumnos del secundario (sin repetir nombres): {Funciones.printlist(highschool_list)}")

print(f"Nombres en comun entre la lista de alumnos de primaria y secundaria: {Funciones.intersection(primary_list,highschool_list)}")
print(f"Nombres que solo se encuentran el la lista de nivel primario: {Funciones.diference(primary_list,highschool_list)}")

# Exercise 7
ocurreces = {}
for string in range(50):
    user_input = input("Ingrese un string: ")
    for char in user_input:
        if char in ocurreces:
            ocurreces[char] += 1
        else:
            ocurreces[char] = 1

for char, count in ocurreces.items():
    print(f"'{char}': {count}")

# Exercise 8
rows = 3
columns = 3
goals = [[0 for point_1 in range(columns)] for point_2 in range(rows)]
points = [0 for point_2 in range(rows)]
goals_difference = [0 for point_2 in range(rows)]
goals_against = [0 for point_2 in range(rows)]

for goals_F in range(rows):
    total_points = 0
    for goals_C in range(columns):
        if goals_F != goals_C:
            total_goals = int(input(f"Ingrese el resultado del equipo {goals_F+1} contra {goals_C+1}: "))
            points[goals_F] += total_goals
            goals[goals_F][goals_C] = total_goals

for goals_F in range(rows):
    victory = 0
    defeat = 0
    tie = 0    
    for goals_C in range(columns):
        if goals_F != goals_C:
            if goals[goals_F][goals_C] > goals[goals_C][goals_F]:
                victory += 1
            elif goals[goals_F][goals_C] == goals[goals_C][goals_F]:
                tie += 1
            else:
                defeat += 1
    print(f"Equipo {goals_F+1} - Victorias: {victory} - Derrotas: {defeat} - Empates: {tie}")

for goals_F in range(rows):
    for goals_C in range(columns):
        if goals_F != goals_C:
            goals_against[goals_F] += (goals[goals_C][goals_F])

for goals_F in range(rows):
    if points[goals_F] > goals_against[goals_F]:
        goals_difference[goals_F] = points[goals_F] - goals_against[goals_F]
    else:
        goals_difference[goals_F] = goals_against[goals_F] - points[goals_F]

for goals_F in range(rows):
    print(f"Puntos totales del Equipo {goals_F+1} : {points[goals_F]}")
    print(f"Goles que le hicieron al equipo {goals_F+1} : {goals_against[goals_F]}")
    print(f"Diferencias de goles hechos con los que le hicieron al equipo {goals_F+1} : {goals_difference[goals_F]}")

# Exercise 9
# Creacion de la tabla y contadores 
memotest_rows = 2
memotest_columns = 3
count = 0
pairs = memotest_columns
count_find = 0

nums_rows = []
nums_columns = []

# Creo dos listas de filas y columnas y les agrego numeros
for i in range(memotest_columns):
    count += 1
    nums_rows.append(count)
    nums_columns.append(count)

# Mezclo las listas por separado
random.shuffle(nums_rows)
random.shuffle(nums_columns)

# Creo una nueva lista que contiene elementos de ambas listas
combined = []
for row, col in zip(nums_rows, nums_columns):
    combined.append(row)
    combined.append(col)

# Creo la matriz del memotest
memotest = [[0 for pair_1 in range(memotest_columns)] for pair_2 in range(memotest_rows)]

# Le asigno los valores a la matriz
for mrows in range(memotest_rows):
    for mcolumns in range(memotest_columns):
        if combined:
            memotest[mrows][mcolumns] = combined.pop(0)

while True:
    print("Bienvenido a Memotest")
    print("1. Jugar")
    print("2. Salir")
    choice = input("Ingrese su opcion: ")

    if choice == "1":

        print("Tablero: ")
        for row in memotest:
            for col in row:
                print("x", end=" ")
            print()

        while True:
            selected_coordinates = [] # Esta lista es para no poder colocar las mismas coordenadas 2 veces
            print(f"Ha encontrado {count_find} parejas, le quedan {pairs} parejas para encontrar todas")

            row_selection = int(input("Ingrese la posicion de la fila (0,1): "))
            col_selection = int(input("Ingrese la posicion de la columna (0,8): "))
            
            selected_coordinates.append([row_selection, col_selection]) # Agrego las coordenadas a la lista

            # Si los numeros que elegi son mayores a 0 y menores que la longitud del memotest o en el caso de la columna si es menor a la longitud de la fila del memotest
            if 0 <= row_selection < len(memotest) and 0 <= col_selection < len(memotest[row_selection]): 
                print(f"Numero en la fila {row_selection} y columna {col_selection}: ")
                print(memotest[row_selection][col_selection])
                row_selection_pair = int(input("Ingrese la posicion de la fila para buscar a la pareja del numero que encontro: "))
                col_selection_pair = int(input("Ingrese la posicion de la columna para buscar a la pareja del numero que encontro: "))

                # Comparo si no estan los segundos valores en la lista de coordenadas
                if ([row_selection_pair,col_selection_pair]) in selected_coordinates:
                    print("Ya ingreso esas coordenadas")
                    continue
                
                # Hago la misma comparacion que hice anteriormente pero con los segundos valores
                if 0 <= row_selection_pair < len(memotest) and 0 <= col_selection_pair < len(memotest[row_selection_pair]) :
                    print(f"Numero en la fila {row_selection_pair} y columna {col_selection_pair}: ")
                    print(memotest[row_selection_pair][col_selection_pair])
                    # En caso de que sean iguales los valores y ninguno de los dos sea un string vacio se ejecuta este condicional
                    if ((memotest[row_selection][col_selection] == memotest[row_selection_pair][col_selection_pair]) and (memotest[row_selection][col_selection] != "") and (memotest[row_selection_pair][col_selection_pair] != "")):
                        print("Felicidades! Encontro a la pareja de este numero")
                        # Contador de las parejas que me quedan
                        pairs -= 1
                        # Si encontre el par, elimino ambos numeros actuales por un string vacio
                        memotest[row_selection][col_selection] = "" 
                        memotest[row_selection_pair][col_selection_pair] = ""
                        # Contador de parejas que he acertado
                        count_find += 1
                        print("Tablero: ")
                        for row in range(len(memotest)):
                            for col in range(len(memotest[row])):
                                # En caso de que la posicion sea distinto de un string vacio me imprime una "x" si no me imprime un 0
                                if memotest[row][col] != "":  
                                    print("x", end=" ")
                                else:
                                    print("0",end=" ")
                            print()
                        if pairs == 0:
                            print("¡Encontro todas las parejas!")
                            break
                    else:
                        print("Pareja incorrecta")
                        for row in range(len(memotest)):
                            for col in range(len(memotest[row])):
                                if memotest[row][col] != "":
                                    print("x", end=" ")
                                else:
                                    print("0",end=" ")
                            print()
                else:
                    print("Numero fuera de rango")
            else:
                print("Numero fuera de rango")
    
    elif choice == "2":
        print("Gracias por jugar")
        break
    else:
        print("Ingrese una opcion valida")

#Exercise 10
row_and_column = 3

matrix = [[0 for column in range(row_and_column)] for row in range(row_and_column)]

for row in range(row_and_column):
    for column in range(row_and_column):
        matrix[row][column] = int(input(f"Ingrese el numero de la fila {row+1} y columna {column+1}: "))

print("Matriz comun:")
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column], end=" ")
    print()

print()

print("Diagonal principal: ")
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if row == column:
            print(matrix[row][column],end=" ")

print()

print("Diagonal inversa")
for element in range(row_and_column - 1, -1, -1):
    print(matrix[row_and_column - 1 - element][element], end=" ")

# Exercise 11
badge = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
badge_choice = input("Ingrese el nombre de una divisa: ").title()

if badge_choice in badge:
    for key, value in badge.items():
        if badge_choice == key:
            print(f"El simbolo de la divisa {key} es {value}")
else:
    print("Divisa no encontrada")

# Exercise 12
information = {}
information[0] = input("Ingrese su nombre: ").title()
information[1] = int(input("Ingrese su edad: "))
information[2] = input("Ingrese su direccion: ").title()
information[3] = int(input("Ingrese su numero de telefono: "))

print(f"{information[0]} tiene {information[1]} años, vive en {information[2]} y su número de teléfono es {information[3]}")

# Exercise 13
fruit_diccionary = {"banana": 300, "pera": 500, "frutilla": 700, "naranja": 900, "mandarina": 1100 }

fruit = input("Ingrese la fruta: ").lower()

if fruit in fruit_diccionary.keys():
    weight = float(input("Ingrese la cantidad de kilos que quiere el usuario: "))
    for key, value in fruit_diccionary.items():
        if fruit == key:
            price = weight * value
            print(f"El precio del kilo de {key} es {value}, el cliente va a llevar {weight} kilo/kilos. El total a pagar es {price}")
else:
    print("La fruta no esta en la lista")