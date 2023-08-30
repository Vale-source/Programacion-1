#Ejercicio 1
lugares = int(input("Ingrese el numero de lugares a mover: "))

for i in range(5) :
    clave = input("Ingrese la palabra a encriptar: ")
    clave = clave.upper()
    encrpit = ""
    for c in clave:
        c = ord(c)
        if (c >= 65) and (c <= 90):
            c = c + lugares
            c = chr(c)
            encrpit += c
        else :
            c = chr(c)
            encrpit += c
    print(encrpit)

#Ejercicio 2

x = 1
cont_pares = 0
cont_impares = 0
while x != 0:
    x = int(input("Ingrese un numero entero positivo: "))
    z = x
    pares = 0
    impares = 0
    while z > 0:
        digito = z % 10
        if digito % 2 == 0:
            pares += 1
            cont_pares += 1
        else:
            impares += 1
            cont_impares += 1
        z //= 10
    print(f"el numero {x} tiene {pares} digitos pares y {impares} digitos impares")

print(f"Se han contado un total de {cont_pares} digitos pares y {cont_impares} digitos impares")
