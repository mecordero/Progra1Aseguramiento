
def bisiesto(año):
    '''
    Entrada: int año
    Salida: True si el año es bisisesto, False si no lo es.
    Proceso: si el año no termina en 00, si sus ultimos 2 digitos son multiplos de 4
             si termina en 00, es bisiesto si es divisible entre 400
    '''
    
    if año%100!=0:
        if (año%100)%4==0:
            return True
        else:
            return False
    elif año%100==0:
        if año%400==0:
            return True
        else:
            return False


def fecha_es_valida(tupla):
    '''
    Entradas: dia,mes y año
    Salidas: True o False si la fecha es valida o invalida
    '''
    año=tupla[0]
    mes=tupla[1]
    dia=tupla[2]

    if año>=0:
        if 1<=mes<=12:
            if mes==2:
                if bisiesto(año)==True:
                    if dia<=29:
                        return True
                    else:
                        return False
                else:
                    if dia<=28:
                        return True
                    else:
                        return False
            if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                if dia<=31 and dia>=1:
                    return True
                else:
                    return False
            if mes==4 or mes==6 or mes==9 or mes==11:
                if dia<=30 and dia>=1:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def dia_siguiente(fecha):
    if fecha [1] == 1 or fecha [1] == 3 or fecha [1] == 5 or fecha[1] == 7 or fecha[1] == 8 or fecha[1] == 10:
        if fecha[2] < 31:
            return (fecha[0], fecha [1], fecha[2] + 1)
        return (fecha[0], fecha[1] + 1, 1)
    if fecha [1] == 2:
        if fecha[2] < 28:
            return (fecha[0], 2, fecha [2] + 1)
        else:
            if fecha[2] == 28 and bisiesto(fecha[0]):
                return (29, 2, fecha[2])
            return (fecha[0], 3, 1)
    if fecha[1] == 4 or fecha[1] == 6 or fecha [1] == 9 or fecha[1] ==11:
        if fecha[2] < 30:
            return (fecha[0], fecha [1], fecha[2] + 1)
        return (1, fecha[1] + 1, fecha[2])
    if fecha[1] == 12:
        if fecha[2] < 31:
            return (fecha[0], fecha [1], fecha[2] + 1)
        return (fecha[0] + 1, 1, 1)
            


