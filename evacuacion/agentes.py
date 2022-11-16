import mesa
from .walk import Walk

class Civil(Walk):
    def __init__(self, unique_id: int, posIni, pos, posFin, model, edad, evacuado, tiempoEvacuado, conoceRuta, puntoEncuentro, moore):
        super().__init__(unique_id, model, pos, moore = moore)
        self.pos = pos
        self.posIni = posIni
        self.posFin = posFin
        self.edad = edad
        self.evacuado = evacuado
        self.tiempoEvacuado = tiempoEvacuado
        self.conoceRuta = conoceRuta
        self.puntoEncuentro = puntoEncuentro
        if self.edad >= 13 and self.edad <45:
            self.rapidez = 5.0
        else:
            self.rapidez = 2.5
        

        
    def step(self):

        if self.rapidez == 5.0:
            self.movimiento(Camino,Obstaculo)
        else:
            self.rapidez = 5.0
            
        if self.pos == self.posFin:
            self.evacuado = True

            

class Camino(mesa.Agent):
    def __init__(self, unique_id: int, model, pos):
        super().__init__(unique_id, model,pos)
            
class Obstaculo(mesa.Agent):
    def __init__(self, unique_id: int, model, pos):
        super().__init__(unique_id, model,pos)


