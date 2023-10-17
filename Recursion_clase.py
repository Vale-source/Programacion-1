# Exercise 1
def Uli_escape(n):
    import random
    ways = [1,2,3]
    choice = random.choice(ways)
    if choice == 1:
        print("El Uli eligio el camino 1, luego de 3 minutos vuelve a la jaula")
        n += 3
        return Uli_escape(n)
    elif choice == 2:
        print("El Uli eligio el camino 2, luego de 5 minutos vuelve a la jaula")
        n += 5
        return Uli_escape(n)
    elif choice == 3:
        print ("El Uli eligio el camino 3, luego de 7 minutos logro salir")
        n += 7
        return n

minute = 1
print(f"El Uli tardo {Uli_escape(minute)} minutos")

# Exercise 2
# Crear una funcion recursiva que que tome un valor entero como parametro y que retorne el numero dado vuelta
def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

num = 5798
print(f"{f(num)}")
