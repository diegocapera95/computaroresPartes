
class Parte:
    def __init__(self, id, nombre, descripcion, id_computador):
        self.id = id
        self.nombre =  nombre
        self.descripcion = descripcion
        self.id_computador = id_computador

class Computador:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre =  nombre
        self.descripcion = descripcion