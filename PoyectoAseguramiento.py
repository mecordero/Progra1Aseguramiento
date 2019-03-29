
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


