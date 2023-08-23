fecha = [input("Dia de la semana: "),int(input("Numero del dia: ")),int(input("Numero del Mes: "))]

fecha[0] = fecha[0].title()

if (fecha[0] == "Lunes") or (fecha[0] == "Martes") or (fecha[0] == "Miercoles") and (fecha[1] < 31 and fecha[1] > 0) and (fecha[2] < 12 and fecha[2] > 0 ) :
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
            
elif fecha[0] == ("Jueves") and (fecha[1] < 31 and fecha[1] > 0) and (fecha[2] < 12 and fecha[2] > 0 ):
    asistencia = int(input("Ingrese el porcentaje de personas que asistieron: "))

    if asistencia > 50:
        print("Asistio la mayoria")
    elif asistencia == 50:
        print("Asistieron la mitad")
    else:
        print("Asistio menos de la mayoria")

elif fecha[0] == ("Viernes") and (fecha[1] == 1) and (fecha[2] == 1 or fecha[2] == 7 ):

    print("Comienzo de nuevo ciclo")
    alumnos = int(input("Ingrese la cantidad de alumnos nuevos: "))
    arancel = float(input("Ingrese el valor del arancel individual: "))
    arancel_total = alumnos * arancel
    print("El arancel total es de: ",arancel_total,"$")

else:
    print("Ingrese fecha valida")

