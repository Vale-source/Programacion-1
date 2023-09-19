# El ejercicio ya esta corregido, el problema era que en las funciones tomaba el valor de
# x e y en vez de los valores de a y b
def most(a,b):
    if (a>b): # En esta linea estaba colocado (x>y)
        return a
    else:
        return b

def least(a,b):
    if (a<b): # En esta linea estaba colocado (x<y)
        return a
    else:
        return b

x = int(input("Un numero: "))
y = int(input("Otro numero: "))

print(most(x-3, least(x+2, y-5)))