fecha = input("Ingrese la fecha en formato 'dia de la semana, numero del dia y numero del mes en formato dia, DD/MM: ")
fecha = fecha.title()

dia_semanas = fecha[0:fecha.find(",")]
dia_numero = int(fecha[fecha.find(" ")+1:fecha.find("/")])
dia_mes = int(fecha[fecha.find("/")+1:])

if (dia_semanas == "Lunes") or (dia_semanas == "Martes") or (dia_semanas == "Miercoles") and (dia_numero < 31 and dia_numero > 0) and (dia_mes < 12 and dia_mes > 0 ) :
    nivel = input("Ingrese en que nivel se encuentra:")
    nivel = nivel.lower()

    if (nivel == "inicial") or (nivel == "intermedio") or (nivel == "avanzado"):
        r = input("¿Se tomaron examanes ese dia? ")
        r = r.lower()

        if r == "si":
            aprobados = int(input("Indique la cantidad de aprobados: "))
            desaprobados = int(input("Indique la cantidad de desaprobados: "))
            total = aprobados + desaprobados
            print("El porcentaje de aprobados fue del: ",round((aprobados*100/total),0),"%")
            
elif (dia_semanas == "Jueves") and (dia_numero < 31 and dia_numero > 0) and (dia_mes < 12 and dia_mes > 0 ):
    asistencia = int(input("Ingrese el porcentaje de personas que asistieron: "))

    if asistencia > 50:
        print("Asistio la mayoria")
    elif asistencia == 50:
        print("Asistieron la mitad")
    else:
        print("Asistio menos de la mayoria")

elif dia_semanas == ("Viernes") and (dia_numero == 1) and (dia_mes == 1 or dia_mes == 7 ) :
    print("Comienzo de nuevo ciclo")
    alumnos = int(input("Ingrese la cantidad de alumnos nuevos: "))
    arancel = float(input("Ingrese el valor del arancel individual: "))
    arancel_total = alumnos * arancel
    print("El arancel total es de: ",arancel_total,"$")

else:
    print("Ingrese fecha valida")

