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
        matriz_aux = [(["."] * (self.columnas)) for i in range(self.filas)]
        # print(self.matriz_aux)
        # print(self.matriz)
        # print(len(self.matriz[0]))
        # print(self.filas)
        for x in range(self.iteraciones):
            self.limites()
            self.matriz = self.cambios(matriz_aux)
            # for fila in self.matriz:
            #    print(fila)

    def cambios(self, matriz_aux):
        """Aplica las reglas del juego para modificar de viva o muerta las
        celdas de la matriz"""
        # print(self.matriz)
        for n in range(1, self.filas - 1):
            for m in range(1, self.columnas - 1):
                if self.matriz[n][m] == muerta:
                    vivas = 0
                    if self.matriz[n][m - 1] == viva:
                        vivas += 1
                    if self.matriz[n - 1][m - 1] == viva:
                        vivas += 1
                    if self.matriz[n - 1][m] == viva:
                        vivas += 1
                    if self.matriz[n - 1][m + 1] == viva:
                        vivas += 1
                    if self.matriz[n][m + 1] == viva:
                        vivas += 1
                    if self.matriz[n + 1][m + 1] == viva:
                        vivas += 1
                    if self.matriz[n + 1][m] == viva:
                        vivas += 1
                    if self.matriz[n + 1][m - 1] == viva:
                        vivas += 1
                    if vivas == 3:
                        matriz_aux[n][m] = viva
                if self.matriz[n][m] == viva:
                    vivas = 0
                    matriz_aux[n][m] = viva
                    if self.matriz[n][m - 1] == viva:
                        vivas += 1
                    if self.matriz[n - 1][m - 1] == viva:
                        vivas += 1
                    if self.matriz[n - 1][m] == viva:
                        vivas += 1
                    if self.matriz[n - 1][m + 1] == viva:
                        vivas += 1
                    if self.matriz[n][m + 1] == viva:
                        vivas += 1
                    if self.matriz[n + 1][m + 1] == viva:
                        vivas += 1
                    if self.matriz[n + 1][m] == viva:
                        vivas += 1
                    if self.matriz[n + 1][m - 1] == viva:
                        vivas += 1
                    if vivas == 2:
                        matriz_aux[n][m] = viva
                    elif vivas == 3:
                        matriz_aux[n][m] = viva
                    else:
                        matriz_aux[n][m] = muerta

        # print(matriz_aux)
        return matriz_aux

    def limites(self):
        """Comprueba filas y columnas con celdas vivas
        y añade/elimina filas/columnas."""
        flimites = [False] * self.filas
        climites = [False] * self.columnas
        for n in range(self.filas):
            for m in range(self.columnas):
                if self.matriz[n][m] == viva:
                    flimites[n] = True
                    break
        for m in range(self.columnas):
            for n in range(self.filas):
                if self.matriz[n][m] == viva:
                    climites[m] = True
                    break

        # print(flimites)
        # print(climites)
        # Comprobamos que no haya mas de 2 False al principio y final de la
        # listas flimites y climites
        if flimites.index(True) == 2:
            pass
        elif flimites.index(True) < 2:
            for x in range(2 - flimites.index(True)):
                self.filas += 1
                self.matriz.insert(0, ["."] * self.columnas)
        elif flimites.index(True) > 2:
            for x in range(flimites.index(True) - 2):
                self.filas -= 1
                self.matriz.pop(0)
        if flimites[::-1].index(True) == 2:
            pass
        elif flimites[::-1].index(True) < 2:
            for x in range(2 - flimites[::-1].index(True)):
                self.matriz.insert(self.filas, ["."] * self.columnas)
                self.filas += 1
        elif flimites[::-1].index(True) > 2:
            for x in range(flimites[::-1].index(True) - 2):
                self.matriz.pop(self.filas - 1)
                self.filas -= 1

        if climites.index(True) == 2:
            pass
        elif climites.index(True) < 2:
            for x in range(2 - climites.index(True)):
                self.columnas += 1
                for fila in self.matriz:
                    fila.insert(0, ".")
        elif climites.index(True) > 2:
            for x in range(climites.index(True) - 2):
                self.columnas -= 1
                for fila in self.matriz:
                    fila.pop(0)
        if climites[::-1].index(True) == 2:
            pass
        elif climites[::-1].index(True) < 2:
            for x in range(2 - climites[::-1].index(True)):
                for fila in self.matriz:
                    fila.insert(self.columnas, ".")
                self.columnas += 1
        elif climites[::-1].index(True) > 2:
            for x in range(climites[::-1].index(True) - 2):
                for fila in self.matriz:
                    fila.pop(self.columnas - 1)
                self.columnas -= 1

        # print(flimites)
        # print(climites)


if __name__ == "__main__":
    app = Aplicacion()
