import datetime
import os

class Subject:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)


class Observador:
    def update(self):
        raise NotImplementedError

class ObservadorA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        funcion = args[0]
        tiempo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        carpeta = os.path.dirname(__file__)
        eventos = os.path.join(carpeta, 'registro_de_eventos_observador.txt')
        with open(eventos, 'a', encoding='utf-8') as x:
            x.write(f"-{tiempo} : Se realizo la funcion - {funcion} -\n")
        print("Parametros cargados :",*args)