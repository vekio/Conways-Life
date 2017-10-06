#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

import sys

# Conway's life
# Si una celda muerta está rodeada exactamente por 3 celdas vivas, pasa al estado viva.
# Si una celda viva no está rodeada por 2 o 3 celdas vivas, pasa al estado muerta.
# En cualquier otro caso la celda no cambia de estado
# Filas n
# Columnas m

viva = "X"
muerta = "."


class Aplicacion():
    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.fichero = sys.argv[1]
        self.iteraciones = int(sys.argv[2])
        self.filas, self.columnas, self.matriz = self.leer_fichero()

        self.main()

    def leer_fichero(self):
        """Lee el fichero introducido por el usuario. Añadimos 4 filas y
        columnas al dibujo original para hacer nuestro algoritmo."""
        try:
            fichero = open(self.fichero, "r")
        except OSError:
            sys.exit("No se encuentra '{}'".format(self.fichero))
        else:
            f = [linea.strip() for linea in fichero]
            filas = int(f[0])
            columnas = int(f[1])
            matriz = [list(linea) for linea in f[2:]]

            # 2 filas con celdas muertas arriba y debajo del dibujo

            matriz.insert(0, ["."] * columnas)
            matriz.insert(filas + 1, ["."] * columnas)
            matriz.insert(0, ["."] * columnas)
            matriz.insert(filas + 2, ["."] * columnas)

            # 2 columnas con celdas muertas a izquierda y derecha del dibujo
            for fila in matriz:
                fila.insert(0, ".")
                fila.insert(columnas + 1, ".")
                fila.insert(0, ".")
                fila.insert(columnas + 2, ".")

            fichero.close()
            print("--> Lectura de {} correcta.".format(self.fichero))

            return filas + 4, columnas + 4, matriz

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
        self.imprimir()

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

    def get_filas_reales(self):
        """Devuelve el número de filas con celdas vivas. Eliminamos
        las filas extra para el algoritmo"""
        return self.filas - 4

    def get_columnas_reales(self):
        """Devuelve el número de columnas con celdas vivas. Eliminamos
        las columnas extra para el algoritmo"""
        return self.columnas - 4


if __name__ == "__main__":
    app = Aplicacion()
