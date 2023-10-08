#Ingreso de la fecha
fecha = input("- Ingrese la fecha del dia corriente. Utilice el siguiente formato: [dia, DD/MM] \n").lower()

#Variables correspondientes
dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes"]

dia_semana = fecha[0:fecha.find(",")]
dia = fecha[fecha.find(" ")+1:fecha.find("/")]
mes = fecha[fecha.find("/")+1:]

#Convierto el dia y el mes a valor numerico 
dia = int(dia)
mes = int(mes)

#Evaluo si los datos ingresados son validos
if (dia_semana not in dias_validos) or (dia > 31) or (mes > 12):
    print("ERROR: Ha ingresado uno o mas datos invalidos.")
else:
    #Casos para niveles inicial, intermedio y avanzado
    if dia_semana in ["lunes", "martes", "miercoles"]:
        if (dia_semana == "lunes"):
            print("\nLUNES - NIVEL INCIAL:")
        elif (dia_semana == "martes"):
            print("\nMARTES - NIVEL INTERMEDIO:")
        elif (dia_semana == "miercoles"):
            print("\nMIERCOLES - NIVEL AVANZADO")
        
        eleccion = input("Se han tomado exámenes en la fecha ingresada? Ingrese Si o No\n").lower()
        if (eleccion == "no"):
            print("Perfecto, gracias por utilizar el programa.")

        elif (eleccion == "si"):
            print("-Ingrese la cantidad de alumnos aprobados y desaprobados")
            aprobados = int(input("APROBADOS: "))
            desaprobados = int(input("DESAPROBADOS: "))

            porcentajeAprobados = (aprobados / (aprobados + desaprobados)) * 100
            print(".-Según los datos ingresados, ha aprobado el ", porcentajeAprobados, "% de los alumnos")

    #Caso para Practica hablada
    elif (dia_semana == "jueves"):
        print("\nJUEVES - PRACTICA HABLADA:")
        asistencia = input("Ingrese el porcentaje de asistencia de alumnos a la clase: ")
        asistencia = asistencia.replace("%", "")
        asistencia = float(asistencia)

        if (asistencia >= 50):
            print(".-Ha asistido la mayoría de alumnos.")
        else:
            print(".-No han asistido la mayoria de alumnos")
    
    #Caso para Ingles para viajeros en fechas iguales a 1/1 o 1/7
    elif ((dia_semana == "viernes") and (dia == 1) and ((mes == 1) or (mes == 7))):
        print("\nVIERNES - INGLES PARA VIAJEROS:")
        print("--Comienzo de nuevo ciclo--")
        cantidadAlumnos = int(input("-Ingrese la cantidad de alumnos de nuevo ciclo: \n"))
        arancel = input("-Ingrese el monto que deberá arancelar cada alumno (monto en $, ejemplo: $5000): \n")

        arancel = arancel.replace("$", "")
        arancel = float(arancel)
        ingresoTotal = arancel * cantidadAlumnos
        print("\nEl ingreso total que se percibirá es de $", ingresoTotal)
        
    #Caso para Ingles para viajeros en fechas distintas a 1/1 o 1/7
    else:
        print("\nVIERNES - INGLES PARA VIAJEROS:")
        print("--Aun no se abren inscripciones para otro ciclo. Gracias--")