import datetime
import os

def registro_log(func):
    def envoltura(*args, **kwargs):
        tiempo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        resultado = func(*args, **kwargs)
        carpeta = os.path.dirname(__file__)
        eventos = os.path.join(carpeta, 'registro_de_eventos_decorador.txt')
        with open(eventos, 'a', encoding='utf-8') as x:
            x.write(f"-{tiempo} : Se realizo la funcion - {func.__name__} -\n")
        print("evento registrado")
        return resultado
    return envoltura
