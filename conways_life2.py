#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan


from cuadrante import Cuadrante
import sys


class Aplicacion():

    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.fichero = sys.argv[1]
        self.iteraciones = int(sys.argv[2])
        self.matriz = self.leer_fichero()
        # print(len(self.matriz))
        self.main()

    def main(self):
        nivel_raiz = int(pow(len(self.matriz), 0.5)) + 1
        self.cuadrante = self.cuadrante_raiz(nivel_raiz)
        self.iteracion()

    def leer_fichero(self):
        """Lee el fichero introducido por el usuario."""
        try:
            fichero = open(self.fichero, "r")
        except OSError:
            sys.exit("No se encuentra '{}'".format(self.fichero))
        else:
            f = [linea.strip() for linea in fichero]
            filas = int(f[0])
            columnas = int(f[1])
            matriz = [list(linea) for linea in f[2:]]

            if filas > columnas:
                c = pow(2, int(pow(filas, 0.5)) + 1)
            else:
                c = pow(2, int(pow(columnas, 0.5)) + 1)

            while filas != c:
                matriz.insert(filas, ["."] * columnas)
                filas += 1

            while columnas != c:
                for fila in matriz:
                    fila.insert(columnas, ".")
                columnas += 1
            fichero.close()

        return matriz

    def cuadrante_raiz(self, nivel, f=0, c=0):
        if nivel == 1:
            nw = Cuadrante.crear_cuadrante(self.matriz[f][c], nivel - 1)
            ne = Cuadrante.crear_cuadrante(self.matriz[f][c + 1], nivel - 1)
            sw = Cuadrante.crear_cuadrante(self.matriz[f + 1][c], nivel - 1)
            se = Cuadrante.crear_cuadrante(self.matriz[f + 1][c + 1], nivel - 1)
            return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)
        else:
            for x in range(4):
                nw = self.cuadrante_raiz(nivel - 1)
                ne = self.cuadrante_raiz(nivel - 1, c=int((pow(2, nivel) / 2)))
                sw = self.cuadrante_raiz(nivel - 1, f=int((pow(2, nivel) / 2)))
                se = self.cuadrante_raiz(nivel - 1, c=int((pow(2, nivel) / 2)), f=int((pow(2, nivel) / 2)))
            return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)

    def iteracion(self):
        self.cuadrante_raiz.generacion()

if __name__ == "__main__":
    app = Aplicacion()
