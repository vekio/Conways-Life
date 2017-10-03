#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

import sys

# Conway's life
# Si una celda muerta está rodeada exactamente por 3 celdas vivas, pasa al estado viva.
# Si una celda viva no está rodeada por 2 o 3 celdas vivas, pasa al estado muerta.
# En cualquier otro caso la celda no cambia de estado


class Aplicacion():
    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.filas = 0      # n
        self.columnas = 0   # m
        self.fichero = sys.argv[1]
        self.iteraciones = sys.argv[2]
        self.matriz = self.leer_fichero()

        self.main()

    def leer_fichero(self):
        # Lee el fichero introducido por el usuario
        try:
            fichero = open(self.fichero, "r")
        except OSError:
            sys.exit("No se encuentra '{}'".format(self.fichero))
        else:
            f = [linea.strip() for linea in fichero]
            self.filas = int(f[0])
            self.columnas = int(f[1])
            self.matriz = [list(linea) for linea in f[2:]]
            # filas con celdas muertas arriba y debajo del dibujo
            self.matriz.insert(0, ["."] * self.columnas)
            self.matriz.insert(self.filas + 1, ["."] * self.columnas)
            # columnas con celdas muertas a izquierda y derecha del dibujo
            for fila in self.matriz:
                fila.insert(0, ".")
                fila.insert(self.columnas + 1, ".")

            #for fila in self.matriz:
            #  print(fila)

            fichero.close()
            print("--> Lectura de {} correcta.".format(self.fichero))

    def main(self):
        """Metodo principal del programa."""
        for x in self.iteraciones:
            self.cambios()

    def cambios(self):
        """Aplica las reglas del juego para modificar de viva o muerta las
        celdas de la matriz"""



if __name__ == "__main__":
    app = Aplicacion()
