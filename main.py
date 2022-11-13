from random import randint, random
import numpy as np



TIEMPO_TOTAL = 600
MIN_LATITUD = -60
MAX_LATITUD = -30
MIN_LONGITUD = -90
MAX_LONGITUD = -60
TIME_STEP = 5

ALTO = 10
ANCHO = 30


class Zona:
    def __init__(self):
        self.matriz = np.zeros((ALTO,ANCHO),int)

    def print(self):
        print("\n")
        for i in range(ALTO):
            for j in range(ANCHO):
                print("#"," ",end="")
            print("\n")


class Guia:
    def __init__(self,posIni,posFinal,rapidez):
        self.posIni = posIni
        self.posFinal = posFinal
        self.posActual = posIni
        self.rapidez = rapidez
        self.puntoEncuentro = -1

    def printState(self):
        print(self.posIni)
        print(self.posActual)
        print(self.posFinal)
        print(self.puntoEncuentro)

class Civil:
    def __init__(self,posIni,edad,conoceRuta):
        self.posIni = posIni
        #self.posFinal = posFinal
        self.posActual = posIni
        self.edad = edad
        self.velocidad = 3.4
        self.evacuado = False
        self.tiempoEvac = 0.0
        self.conoceRuta = conoceRuta
        self.puntoEncuentro = -1
    
    def printState(self):
        print("posIni: ",self.posIni)
        #print("posActual: "self.posActual)
        #print(self.posFinal)
        print("edad: ",self.edad)
        #print(self.evacuado)
        #print(self.tiempoEvac)
        print("conoce ruta?: ",self.conoceRuta)
        #print(self.puntoEncuentro)
        print("\n")


        
def randomPos():
    latitud = randint(MIN_LATITUD,MAX_LATITUD)
    longitud = randint(MIN_LONGITUD,MAX_LONGITUD)
    return (latitud,longitud)

def randomBoolean(probabilidad):
    return random() < probabilidad

cantidadPersonas = 1000
epocaVacaciones = False
probConocerRuta = 0.4 if epocaVacaciones == True else 0.7
civiles = []
F = 0
T = 0
for i in range(cantidadPersonas):
    civil = Civil(randomPos(),randint(8,99),randomBoolean(probConocerRuta))

zona = Zona()