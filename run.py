#import prueba
import sys
import os
from dao.fabricas import *


def funcionPrincipal():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    opcion = input("¿Bajo que formato desea cargar los datos?\n 1. XML\n 2. JSON\n 3. Salir\n")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    if opcion == '1':
        fabrica = XMLDAOFabrica()
    elif opcion == '2':
        fabrica = JSONDAOFabrica()
    else:
        sys.exit()

    dao_computador = fabrica.crear_dao_computador()
    dao_parte = fabrica.crear_dao_parte()
    opcion = input("""¿Que deseas hacer?
    1. Ver los computadores
    2. Ver las partes de un computador
    3. Ver las partes de todos los computadores
    4. Salir\n""")
    os.system ("cls") 
    if (opcion == '1'):
        computadores = dao_computador.obtener_todos()
        for computador in computadores:
            print("-"*70)
            print(f"Nombre: {computador.nombre}\nDescripción: {computador.descripcion}")

    elif opcion == '2':
        computadores = dao_computador.obtener_todos()
        texto = f"¿De que computador desea ver las partes?\n"
        for index, computador in enumerate(computadores):
            texto += f"{index + 1}. {computador.nombre}\n"

        opcion = input(texto)
        if (not opcion.isdigit()):
            print("No ha ingresado un número válido")
            sys.exit()

        opcion = int(opcion)
        if (opcion < 1 or opcion > len(computadores)):
            print("Opción inválida")
            sys.exit()

        computador = computadores[int(opcion) - 1]
        partes = dao_parte.obtener_por_id_computador(computador.id)
        for parte in partes:
            print("-"*70)
            print(f"Nombre: {parte.nombre}\nDescripción: {parte.descripcion}")
    
    elif opcion == '3':
        partes = dao_parte.obtener_todos()
        for parte in partes:
            computador = dao_computador.obtener(parte.id_computador)
            print("-"*70)
            print(f"Nombre: {parte.nombre}\nDescripción: {parte.descripcion}\nComputador: ({computador.id}, {computador.nombre})")


if __name__ == '__main__':
    funcionPrincipal()


