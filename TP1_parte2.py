#Ejercicio_1
lado1 = 5
lado2 = 8
area = lado1*lado2
print(area)
perimetro = (lado1*2) + (lado2*2)
print(perimetro)

#Ejercicio_2
cateto_adyacente = 3
cateto_opuesto = 4
hipotenusa = ((cateto_adyacente**2) + (cateto_opuesto**2))**(1/2)
print(float(hipotenusa))

#Ejercicio_3
num1 = 5
num2 = 5
suma = num1 + num2
resta = num1 - num2
division = num1//num2
multiplicacion = num1*num2
print(suma, resta, multiplicacion, division)

#Ejercicio_4
Fahrenheit = 32
Celsius = (Fahrenheit - 32)*5/9
print(Celsius)

#Ejercicio_5
#Punto "a)" arreglado:
nombre = "Valentin"
A = input(nombre + " ¿Cual es tu cancion favorita? ")

#Punto "b)" arreglado:
precio = float(input("Precio: "))
total = precio + (precio * 0.1)

#Punto "c)" arreglado:
edad = int(input("Edad: "))
print("tu edad es: ", edad)

#Punto "d" arreglado:
edad = int(input("Edad: ")) 
print("Veamos si tienes 18..." if edad==18 else "Tu edad no es 18")

#Ejercicio_6
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
media = (num1 + num2 + num3) / 3
print("La media de los 3 numeros ingresados es: ",media)

#Ejercicio_7
min = int(input("Ingrese una cantidad de minutos: "))
horas = min//60
minutos = min%60
print(horas, "horas y",minutos,"minutos")

#Ejercicio_8
sueldo = float(input("Ingrese su sueldo base: "))
monto_total = float(input("Ingrese el monto total de las 3 ventas: "))
comision = monto_total*0.1
sueldo_total = sueldo + comision
print("El sueldo total con comisiones incluidas es de: ",sueldo_total)

#Ejercicio_9
compra = float(input("Monto a pagar: "))
descuento = compra - (compra*0.15)
print("El total a pagar con descuento es: ",descuento)

#Ejercicio_10
parcial_1 = 65
parcial_2 = 90
parcial_3 = 40
prom_parcial = ((parcial_1 + parcial_2 + parcial_3)/3)
examen_final = 80
trabajo_final = 70
calificacion_final = prom_parcial*0.55 + examen_final*0.35 + trabajo_final*0.1
print("La calificacion final es de: ",calificacion_final)

#Ejercicio_11
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
distancia = abs(num1 - num2)
print("La distancia entre ambos numeros es:",distancia)

#Ejercicio_12
num = 9
print("la raiz cuadrada de",num,"es",num**(1/2),"y la raiz cubica es",num**(1/3))

#Ejercicio_13
num = int(input("Ingrese un numero de dos cifras: "))
num_primera_cifra = str(num//10)
num_segunda_cifra = str(num%10)
print("El numero invertido es:",num_segunda_cifra + num_primera_cifra)

#Ejercicio_14
A = float(input("Ingrese la variable A: "))
B = float(input("Ingrese la variable B: "))
aux = A
A = B
B = aux
print("El valor de la variable A es:",A)
print("El valor de la variable B es",B)

#Ejercicio_15
H = int(input("Hora: "))
M = int(input("Minutos: "))
S = int(input("Segundos: "))
T = int(input("Tiempo de viaje (En segundos): "))

#Conversion de tiempo de viaje a segundos, minutos y horas
T_horas = (T/3600)//1
T_minutos = ((T/3600)%1)*60
T_segundos = (T_minutos - (T_minutos//1))*60

#Comienzo con la sumatoria del tiempo

#Realizo la suma de los segundos totales
segundos_total = (T_segundos + S)//1 

#Calculo los minutos extras si tengo mas de 60 segundos
minutos_extras = 0 if segundos_total < 60 else (segundos_total/60)//1 

#En caso de que mis segundos sean menores a 60, mantengo el valor anterior, si no le resto 60 a mis segundos totales
#una cantidad de "N" veces, donde N son la cantidad de minutos extras
segundos_total = segundos_total if segundos_total < 60 else segundos_total - (60 * minutos_extras) 

#Realizo el mismo proceso con los minutos
minutos_total = (minutos_extras + M + T_minutos)//1
horas_extras = 0 if minutos_total < 60 else (minutos_total/60)//1
minutos_total = minutos_total if minutos_total < 60 else minutos_total - (60 * horas_extras)

#Sumo el total de mis horas
horas_total = (horas_extras + H + T_horas)//1

print("Tiempo de viaje:",int(horas_total),"Horas",int(minutos_total),"minutos",int(segundos_total),"Segundos")

#Ejercicio_16
nombre = input("Ingres su nombre: ")
apellido_1 = input("Ingrese su primer apellido: ")
apellido_2 = input("Ingrese su segundo apellido: ")

print("Las inciales son:",nombre[0] + apellido_1[0] + apellido_2[0])

#Ejercicio_17
usuario = input("Ingrese su nombre: ")
print(f"Ahora estas en la matrix {usuario}")

#Ejercicio_18
cena = float(input("Ingrese el costo de la cena: "))
servicio = float(cena * 0.062)
propina = float(cena * 0.1)
print("Monto total a pagar:",cena + servicio + propina)

#Ejercicio_19
dia = int(input("Ingrese el dia de su nacimiento: "))
dia = dia if dia > 10 else "0" + str(dia)
mes = int(input("Ingrese el mes de su nacimiento: "))
mes = mes if mes > 10 else "0" + str(mes)
año = int(input("Ingrese el año de su nacimiento: "))
print("Fecha de nacimiento:",dia,"/",mes,"/",año)

#Ejercicio_20
fecha_nacimiento = input("Ingrese su fecha en formato DDMMAAAA: ")
print("Fecha de nacimiento:",fecha_nacimiento)

#Ejercicio_21
litros_kilometro = float(input("Ingrese la cuantos km puede recorrer su moto con 1 litro: "))
capacidad = float(input("Ingrese la capacidad de litros que tiene el tanque: "))
km_recorrer = float(input("Ingrese la cantidad de kilometros a recorrer: "))

#Aplique regla de 3 para conocer cuanto puedo recorrer con el tanque completo
#luego dividi los kilometros a recorrer por los kilometros que puede hacer un tanque
#para conocer los litros necesarios
tanques_necesarios = km_recorrer/(capacidad * litros_kilometro)
print("La cantida de tanques necesarios para",km_recorrer,"Km son",float(round(tanques_necesarios,1)))