from dao.access_objects import *

class DAOFabrica:
    def crear_dao_computador(self):
        pass

    def crear_dao_parte(self):
        pass

class XMLDAOFabrica(DAOFabrica):
    def crear_dao_computador(self):
        return XMLComputadorDAO()

    def crear_dao_parte(self):
        return XMLParteDAO()


class JSONDAOFabrica(DAOFabrica):
    def crear_dao_computador(self):
        return JSONComputadorDAO()

    def crear_dao_parte(self):
        return JSONParteDAO()