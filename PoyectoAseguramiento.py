
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


def fecha_es_valida(año,mes,dia):
    '''
    Entradas: dia,mes y año
    Salidas: True o False si la fecha es valida o invalida
    '''

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

#8 Fecha
def fecha(num):
    '''
    Entradas: numero que corresponde a el dia, mes y el año
    Salidas: el dia, el mes y el año
    Proceso: determinar el mes dependiendo del digito ingresado
    Restricciones: no hay
    '''

    if valida_fecha(num)== True:
        if Mes==1:
            meses="Enero"
        if Mes==2:
            meses="Febrero"
        if Mes==3:
            meses="Marzo"
        if Mes==4:
            meses="Abril"
        if Mes==5:
            meses="Mayo"
        if Mes==6:
            meses="Junio"
        if Mes==7:
            meses="Julio"
        if Mes==8:
            meses="Agosto"
        if Mes==9:
            meses="Setiembre"
        if Mes==10:
            meses="Octubre"
        if Mes==11:
            meses="Noviembre"
        if Mes==12:
            meses="Diciembre"
        return (Dia, meses, Año)
    else:
        return False
