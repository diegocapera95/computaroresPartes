import json
import xmltodict
import os.path
from dao.transfer_objects import *

class ComputadorDAO:
    def obtener_todos(self):
        pass

    def obtener(self, id):
        pass

    def guardar(self):
        pass

class ParteDAO:
    def obtener_todos(self):
        pass

    def obtener(self, id):
        pass

    def obtener_por_id_computador(self, id_computador):
        pass

    def guardar(self):
        pass

class XMLComputadorDAO(ComputadorDAO):
    def obtener_todos(self):
        ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'recursos', 'bd.xml'))
        with open(ruta) as f:
            data = xmltodict.parse(f.read())
        return [Computador(int(c['id']), c['nombre'], c['descripcion']) for c in data['root']['computadores']]

    def obtener(self, id):
        return next((x for x in self.obtener_todos() if x.id == id), None)

    def guardar(self):
        pass

class JSONComputadorDAO(ComputadorDAO):
    def obtener_todos(self):
        ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'recursos', 'bd.json'))
        with open(ruta) as f:
            data = json.load(f)
        return [Computador(c['id'], c['nombre'], c['descripcion']) for c in data['computadores']]

    def obtener(self, id):
        return next((x for x in self.obtener_todos() if x.id == id), None)

    def guardar(self):
        pass

class XMLParteDAO(ParteDAO):
    def obtener_todos(self):
        ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'recursos', 'bd.xml'))
        with open(ruta) as f:
            data = xmltodict.parse(f.read())
        return [Parte(int(p['id']), p['nombre'], p['descripcion'], int(p['id_computador'])) for p in data['root']['partes']]

    def obtener(self, id):
        return next((x for x in self.obtener_todos() if x.id == id), None)

    def obtener_por_id_computador(self, id_computador):
        return [p for p in self.obtener_todos() if p.id_computador == id_computador]

    def guardar(self):
        pass

class JSONParteDAO(ParteDAO):
    def obtener_todos(self):
        ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'recursos', 'bd.json'))
        with open(ruta) as f:
            data = json.load(f)
        return [Parte(p['id'], p['nombre'], p['descripcion'], p['id_computador']) for p in data['partes']]

    def obtener(self, id):
        return next((x for x in self.obtener_todos() if x.id == id), None)

    def obtener_por_id_computador(self, id_computador):
        return [p for p in self.obtener_todos() if p.id_computador == id_computador]

    def guardar(self):
        pass