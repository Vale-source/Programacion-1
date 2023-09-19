import funciones_sumar_digitos_2_cifras

number = int(input("Numero a procesar: "))
aux = number

while number != 0:
    print(f"Suma: {funciones_sumar_digitos_2_cifras.add_digitis(number)}")
    number = int(input("Ingrese el numero: "))
    aux += number
print(f"La suma de los numeros ingresados es {aux} y la suma de sus digitos es {funciones_sumar_digitos_2_cifras.add_digitis(aux)}")

