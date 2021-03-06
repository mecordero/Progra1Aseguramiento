def fecha_es_tupla(fecha):
    '''
    Entrada: fecha en forma de tupla (int, int, int)
    Salida: true o false dependiendo si el formato de la fecha es valida
    Proceso: valida que el tipo de los datos ingresados sea correcta
    '''
    if isinstance(fecha, tuple) == False:
        return False
    #Valida que el parametro sea una tupla de 3 digitos
    if len(fecha) != 3:
        return False
    #Valida que los parametros sean enteros
    if isinstance(fecha[0], int) and isinstance(fecha[1], int) and isinstance(fecha[2], int):
        return True
    return False

def bisiesto(anho):
    '''
    Entrada: int año
    Salida: True si el año es bisiesto, False si no lo es.
    Proceso: si el año no termina en 00, si sus ultimos 2 digitos son multiplos de 4 si termina en 00, es bisiesto si es divisible entre 400
    '''
    #Valida que el parámetro sea un entero
    if not isinstance(anho, int):
        return False
    #Revisa los casos donde el año termina en 00
    if anho%100 != 0:
        if (anho%100)%4 == 0:
            return True
        return False
    #Revisa los casos donde el año no termina en 00
    elif anho%100 == 0:
        if anho%400 == 0:
            return True
        return False


def fecha_es_valida(tupla):
    '''
    Entradas: fecha en forma de tupla (int, int, int)
    Salidas: True o False si la fecha es valida o invalida
    Proceso: Verifica si la fecha existe en el calendario
    '''

    if fecha_es_tupla(tupla) == False:
        return False
    
    anho = tupla[0] #Año de la fecha
    mes = tupla[1] #Mes de la fecha
    dia = tupla[2] #Dia de la fecha

    if anho >= 1582: #Valida que el año ingresado sea un número positivo
        if 1 <= mes <= 12: #Valida que el mes este entre 1 y 12
            if mes == 2: #Caso especial para validar febrero por si es bisiesto
                if bisiesto(anho) == True:
                    if dia <= 29:
                        return True
                    return False
                elif dia <= 28:
                    return True
                return False
            if mes in (1, 3, 5, 7, 8, 10, 12):#Para los meses de 31 días
                if dia <= 31 and dia >= 1: #Si no se sale del rango entre 1 y 31
                    return True
                return False
            if mes in (4, 6, 9, 11): #Para los meses de 30 días
                if dia <= 30 and dia >= 1: #Si no se sale del rango entre 1 y 30
                    return True
                return False
            return False
        return False
    print("Ingresar año mayor o igual al 1582")
    return False


def dia_siguiente(fecha):
    '''
    Entrada: fecha en forma de tupla (int, int, int)
    Salida: fecha en forma de tupla (int, int, int) con la fecha siguiente a la ingresada
    Proceso: Devuelve la fecha siguiente a la ingresada 
    '''
    #Para los meses de 31 días
    if fecha[1] == 1 or fecha[1] == 3 or fecha[1] == 5 or fecha[1] == 7 or fecha[1] == 8 or fecha[1] == 10:
        if fecha[2] < 31:
            return (fecha[0], fecha[1], fecha[2] + 1)
        return (fecha[0], fecha[1] + 1, 1)
    #Para febrero
    if fecha[1] == 2:
        if fecha[2] < 28:
            return (fecha[0], 2, fecha[2] + 1)
        elif fecha[2] == 28 and bisiesto(fecha[0]):
            return (fecha[0], 2, 29)
        return (fecha[0], 3, 1)
    #Para los meses con 30 días
    if fecha[1] == 4 or fecha[1] == 6 or fecha[1] == 9 or fecha[1] == 11:
        if fecha[2] < 30:
            return (fecha[0], fecha[1], fecha[2] + 1)
        return (fecha[0], fecha[1] + 1, 1)
    #Para diciembre por el caso del 31 de diciembre
    if fecha[1] == 12:
        if fecha[2] < 31:
            return (fecha[0], fecha[1], fecha[2] + 1)
        return (fecha[0] + 1, 1, 1)


def dias_desde_primero_enero(fecha):
    '''
    Entrada: fecha en forma de tupla (int, int, int)
    Salida: número de días en forma de int
    Proceso: Devuelve el número de días entre el primero de enero y la fecha dada
    '''
    #Verifia si la fecha es válida
    if fecha_es_valida(fecha):
        #Ciclo en el cual suma los días entre el primero de enero y la fecha dada
        if fecha[1] == 1:
            return fecha[2]-1
        else:
            diferencia_de_dias = -1
            for i in range(1, fecha[1]):
                diferencia_de_dias += dias_de_mes((fecha[0], i, fecha[2]))
            return diferencia_de_dias + fecha[2]                     
    else:
        print("Digite una fecha válida" + str(fecha))

def dia_primero_enero(anho):
    '''
    Entrada: fecha en forma de tupla (int, int, int)
    Salida: Devuelve el número que representa el dia de la semana.
    Proceso: Devuelve el primer día del mes (0=Domingo, 1=Lunes, 2=Martes, 3=Miércoles, 4=Jueves, 5=Viernes, 6=Sábado)
    '''

    mes = 1 #Mes de enero
    dia = 1 #Número de día
    anho -= 1 #Se debe decrementar en 1 el año al utilizar el mes de enero
    cent = anho // 100 #Calculo del siglo
    year = anho % 100  #Año de ese siglo

    #Fórmula para el cálculo del dia
    dia_de_semana = (1 + int(2.6*11 - 0.2) - 2*cent + year + year//4 + cent//4)%7
    return dia_de_semana   

def imprimir_3x4(anho):
    '''
    Entrada: int año
    Salida: None
    Proceso: devuelve el calendario del año ingresado con los meses y si el nombre del dia por fecha
    '''
    if not isinstance(anho, int) or anho < 1582:
        print("Fecha invalida")
        return
    print("Calendario del año " + str(anho) + " D.C.")


    #Encabezados que imprimir de los grupos de meses
    encabezados = ["         Enero        |        Febrero       |         Marzo        |         Abril      "]
    encabezados += ["         Mayo         |         Junio        |         Julio        |        Agosto      "]    
    encabezados += ["       Setiembre      |        Octubre       |       Noviembre      |       Diciembre    "]  
    
    extra_meses = -4 #variable para saber por cual mes va
    dia_primero_e = dia_primero_enero(anho) #día de la semana del primero de enero del año ingresado

    #FOR de todos los meses
    for encabezado in encabezados:
        print(encabezado)
        print(" D  L  K  M  J  V  S  | D  L  K  M  J  V  S  | D  L  K  M  J  V  S  | D  L  K  M  J  V  S")  
        dias_meses = [1, 1, 1, 1] #variable que lleva el contador del día de cada mes
        extra_meses += 4
        #While no han terminado los 4 meses de imprimirse
        while dias_meses != [0, 0, 0, 0]:
            for i in range(0, 4): #Para cada mes           
                if dias_meses[i] == 0:
                    dia_primero = 0
                else:
                    dia_primero = dias_desde_primero_enero((anho, extra_meses + i + 1, dias_meses[i])) #31
                    dia_primero = (dia_primero + dia_primero_e) % 7 #3
                #imprime espacios sin numero
                for j in range(0, dia_primero):
                    print("   ", end="")
                    continue
            
                #imprime los numeros de los días
                for k in range(dia_primero, 7):
                    if dias_meses[i] == 0:
                        print("   ", end="")
                        continue
                    elif dias_meses[i] < 10:
                        print(" ", end="")
                    print(str(dias_meses[i]) + " ", end="")                

                    #verifica si llegó al máximo

                    if dias_de_mes((anho, extra_meses + i + 1, 1)) == dias_meses[i]:
                        dias_meses[i] = 0
                    else:
                        dias_meses[i] += 1

                if i != 3:
                    print(" |", end="")
                else:
                    print()

##Funciones extra

def dias_de_mes(fecha):
    '''
    Entrada: fecha en forma de tupla (int, int, int)
    Salida: número de días en forma de int
    Proceso: Devuelve el número de días de un mes
    '''
    #Devuelve la cantidad de días de un mes en un año bisiesto
    if bisiesto(fecha[0]):
        if fecha[1] == 2:
            return 29
        elif fecha[1] == 4 or fecha[1] == 6 or fecha[1] == 9 or fecha[1] == 11:
            return 30
        else:
            return 31
    #Devuelve la cantidad de días de un mes en un año
    else:
        if fecha[1] == 2:
            return 28
        elif fecha[1] == 4 or fecha[1] == 6 or fecha[1] == 9 or fecha[1] == 11:
            return 30
        else:
            return 31
