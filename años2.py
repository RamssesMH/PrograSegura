"""
Saber tu tiempo de vida
"""
import time
import argparse
from calendar import isleap
from datetime import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO,
                    filename='app.log',
                    filemode='a')

def _año_bisiesto(dia, mes, año):
    """
    valida si es año bisiesto o no
    Args:
        dia (_int_): _description_
        mes (_int_): _description_
        año (_int_): _description_
    """
    logging.info(f'Se está intentado ver si {año} es un año bisiesto')
    if isleap(año) == False:
         if dia >= 29 and mes == 2:
            print("Esa fecha es invalida")
            logging.exception('Se introdujo una fecha invalida', stack_info=True)
            exit()
    elif isleap(año) and dia>29:
        print("Esa fecha es invalida")
        logging.exception('Se introdujo una fecha invalida', stack_info=True)
        exit()


def _validar_dias_en_meses(dia,mes):
    """
    valida que los meses tengan 30 o 31 dias

    Args:
        dia (_int_): _description_
        mes (_int_): _description_
    """

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

        if (dia<=31 )==False:
            print("El dia es invalido")
            logging.exception('Se introdujo una fecha invalida', stack_info=True)
            exit()
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11 : 
        if (dia>30):
            print("El dia es invalido")
            logging.exception('Se introdujo una fecha invalida', stack_info=True)
            exit()



def validar_no_tener_mas_de_150 (año):
    """
    Valida que no tengas mas de 150 años

    Args:
        año (_int_): _description_
    """
    fecha_hoy= datetime.today().strftime('%d-%m-%Y')
    fecha_desglo = fecha_hoy.split('-')
    año_actual = fecha_desglo[2]
    año_act = _convertir_a_entero(año_actual)
    if año_act - año >= 150:
        print("la peorsona no puede tener mas de 150 años")
        logging.exception('Se introdujo una fecha mayor a 150 años', stack_info=True)
        exit()


def no_pasar_fecha_actual(dia, mes, año):
    """
    Valida si la fecha no es mayor o igual a la fecha actual

    Args:
        dia (_int_): _description_
        mes (_int_): _description_
        año (_int_): _description_
    """

    fecha_hoy= datetime.today().strftime('%d-%m-%Y')
    fecha_desglo = fecha_hoy.split('-')

    año_actual = fecha_desglo[2]
    año_act = _convertir_a_entero(año_actual)
    mes_actual = fecha_desglo[1]
    mes_act = _convertir_a_entero(mes_actual)
    dia_actual = fecha_desglo[0]
    dia_act = _convertir_a_entero(dia_actual)
    
    if año>año_act:
        print("Tienes que poner una fecha anterior al dia de hoy")
        logging.exception('Introdujo una fecha futura o la actual', stack_info=True)
        exit()
    elif año == año_act:

        if mes>mes_act:
            print("Tienes que poner una fecha anterior al dia de hoy")
            logging.exception('Introdujo una fecha futura o la actual', stack_info=True)
            exit()
        elif mes == mes_act:
            if dia > dia_act:
                print("Tienes que poner una fecha anterior al dia de hoy")
                logging.exception('Introdujo una fecha futura o la actual', stack_info=True)
                exit()


def _validar_no_tener_numeros_negativos (dia,mes,año):
    if dia <= 0 or mes <=0 or año<=0:
        print("uno o mas datos que pusiste son negativos")
        logging.exception('uno o mas datos que se introdijeron son negativos', stack_info=True)
        exit()

def _convertir_a_entero(cadena: str):
    """
    Trata de convertir una cadena a un número entero, regresa None en caso de que la conversión no sea posible.

    Keyword Arguments:
    cadena: str
    returns: int, None (en caso de error)
    """
    if cadena.isnumeric():
        return int(cadena)
    else:
        print ("ingresa una fecha valida")
        logging.exception('Se introdujo una fecha invalida', stack_info=True)
        exit()


def calcula_tiempo(dia,mes,año):
    """
    calcula tu tiempo de vida
    Args:
        dia (_int_): _description_
        mes (_int_): _description_
        año (_int_): _description_
    """
    logging.info(f'Se está intentado calcular la fecha')
    edad = relativedelta(datetime.now(), datetime(año, mes, dia))
    tiempo = time.strftime('%H:%M:%S', time.localtime())
    tiemSplit = tiempo.split(':')
    print("El tiempo que ha pasado desde tu fecha de nacimiento es "f"{edad.years} años, {edad.months} meses, {edad.days} días, "+tiemSplit[0]+" horas, "+ tiemSplit[1]+ " minutos y "+tiemSplit[2]+" segundos")

    

    
if __name__ == '__main__':
    all_args =  argparse.ArgumentParser()
    all_args.add_argument("-d", "--Dia", help="Dia", required=True)
    all_args.add_argument("-m", "--Mes", help="Mes", required=True)
    all_args.add_argument("-a", "--Año", help="Año", required=True)
   
    args = vars(all_args.parse_args())

    dia = _convertir_a_entero(args['Dia'])
    mes = _convertir_a_entero(args['Mes'])
    año = _convertir_a_entero(args['Año'])

    _validar_no_tener_numeros_negativos(dia,mes,año)
    _validar_dias_en_meses(dia,mes)
    validar_no_tener_mas_de_150(año)
    no_pasar_fecha_actual(dia,mes,año)
    _año_bisiesto(dia,mes,año)
    calcula_tiempo(dia,mes,año)


    