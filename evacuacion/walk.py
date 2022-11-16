import mesa


class Walk(mesa.Agent):
    grid = None
    x = None
    y = None
    moore = True

    def __init__(self, unique_id: int, model, pos, moore = True):
        super().__init__(unique_id, model)
        self.pos = pos
        self.moore = moore

    def movimiento(self, objetivo,obstaculo):
        # Pick the next cell from the adjacent cells.
        next_moves = []
        vecinos =  self.model.grid.get_neighbors(self.pos, self.moore, True)
        objetivos = [obj for obj in vecinos if isinstance(obj, objetivo)]
        obstaculos = [obj for obj in vecinos if isinstance(obj, obstaculo)]
        
        #si hay camino para llegar
        if len(objetivos) > 0:
            flag = 0
            for ob in objetivos:
                #si el camino avanza, el proximo mov es por el camino
                if flag == 0 and ob.pos[1] > self.pos[1] :
                     next_move = ob.pos
                     flag = 1
        #Si no hay camino, pero hay obstaculo
        elif len(obstaculo) > 0:
            for vec in vecinos:
                #Se buscan todos los vecinos que no sean obstaculos y luego se selecciona uno al azar
                if vec not in obstaculos:
                    next_moves.append(vec.pos)
            next_move = self.random.choice(next_moves)
        #Si no hay camino, pero tampoco obstaculo se mueve de manera aleatoria
        else:
            next_move = self.random.choice(vecinos.pos)
        # Now move:
        self.model.grid.move_agent(self, next_move)