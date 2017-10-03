#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

import sys

# Conway's life


class Aplicacion():
    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.filas = 0      # n
        self.columnas = 0   # m
        self.fichero = sys.argv[1]
        self.iteraciones = sys.argv[2]
        self.matriz = self.leer_fichero()

    def leer_fichero(self):
        # Lee el fichero introducido por el usuario
        try:
            fichero = open(self.fichero, "r")
        except IOError:
            raise IOError("No se encuentra '{}'").format(self.fichero)
        else:
            f = [linea.strip() for linea in fichero]
            self.filas = int(f[0])
            self.columnas = int(f[1])
            self.matriz = [list(linea) for linea in f[2:]]
        finally:
            fichero.close()
            print("--> Lectura de {} correcta.").format(self.fichero)


if __name__ == "__main__":
    app = Aplicacion()
