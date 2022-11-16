import mesa
import random

from .agentes import Civil, Camino, Obstaculo
from .scheduler import RandomActivationByTypeFiltered


class simulacion(mesa.Model):

    ancho = 100
    alto = 100

    cant_civiles = 500
    cant_caminos = 200
    cant_obstaculos = 50

    puntos_encuentro = 5

    def __init__(
        self,
        ancho = 100,
        alto = 100,
        cant_civiles = 500,
        cant_caminos = 500,
        cant_obstaculos = 50,
        puntos_encuentro = 5,
        ):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.cant_civiles = cant_civiles
        self.cant_caminos = cant_caminos
        self.cant_obstaculos = cant_obstaculos
        self.puntos_encuentro = puntos_encuentro

        self.schedule = RandomActivationByTypeFiltered(self)
        self.grid = mesa.space.MultiGrid(self.ancho,self.alto,True)
        self.datacollector = mesa.DataCollector(
            {
                "Civl": lambda m: m.schedule.get_type_count(Civil),
                "Camino": lambda m: m.schedule.get_type_count(Camino),
                "Obstaculo": lambda m: m.schedule.get_type_count(Obstaculo)
            }
        )

        #crear caminos
        puntos = []
        i = 0
        while i < self.puntos_encuentro:
            x = self.random.randrange(self.ancho)
            if x not in puntos:
                puntos.append(x)
                i+=1
        
        
        cantidad_altura = self.cant_caminos/self.puntos_encuentro
        altura_minima = self.alto - cantidad_altura

        for x in puntos:
            altura_maxima = self.alto -1
            while altura_maxima >= altura_minima:
                camino = Camino(self.next_id,self,(x,altura_maxima))
                self.grid.place_agent(camino, (x,altura_maxima))
                self.schedule.add(camino)
                altura_maxima = altura_maxima - 1
        
        #crear obstaculos
        #X,Y random
        
        for i in range(self.cant_obstaculos):
            x = self.random.randrange(self.ancho)
            y = self.random.randrange(self.alto)
            obstaculo = Obstaculo(self.next_id,self,(x,y))
            self.grid.place_agent(obstaculo, (x, y))
            self.schedule.add(obstaculo)    


        #crear civiles
        #X,Y random, se setean edades y atributos con valores random basados en distintas probabilidades
        #unique_id: int, posIni, pos, posFin, model, edad, evacuado, tiempoEvacuado, conoceRuta, puntoEncuentro, moore
        
        
        for i in range(self.cant_civiles):
            x = self.random.randrange(self.ancho)
            y = self.random.randrange(self.alto)
            minimo = -1
            for punto in puntos:
                dif = abs(x-punto)
                if minimo == -1 or dif<minimo:
                    minimo = dif
                    xfin = punto
            edad = random.randint(13,70)
            evacuado = False
            t_evacuado = 0
            conocer = random.randint(1,100)
            if conocer < 70:
                conoce = True
            else:
                conoce = False
            moore = True
            civil = Civil(self.next_id,(x,y),(x,y),(xfin,self.alto-1),self,edad,evacuado,t_evacuado,conoce,(xfin,self.alto-1),moore)
            self.grid.place_agent(civil, (x, y))
            self.schedule.add(civil)   
        
    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)