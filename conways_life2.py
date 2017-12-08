#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

from time import time
from cuadrante import Cuadrante
import sys


class Aplicacion():

    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.fichero = sys.argv[1]
        self.iteraciones = int(sys.argv[2])
        self.matriz = self.leer_fichero()

        self.tiempo_inicial = time()
        self.tiempo_final = 0
        # print(len(self.matriz))
        # print(self.matriz)
        # for line in self.matriz:
        #    print(line)
        self.main()

    def main(self):
        """Metodo main del programa."""
        nivel_raiz = int(pow(len(self.matriz), 0.5)) + 1
        self.cuadrante = self.cuadrante_raiz(nivel_raiz)
        for x in range(self.iteraciones):
            print("--iteracion ", x)
            self.iteracion()
        self.tiempo_final = time()
        self.imprimir()

    def leer_fichero(self):
        """Lee el fichero introducido por el usuario. Devuelve una matriz
        de tamaño la menor potencia de 2 en la que entra el dibujo del fichero,
        con los valores en cada posicion."""
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
        """Crea el cuadrante raiz de la matriz leida."""
        if nivel == 1:
            if self.matriz[f][c] == "X":
                poblacion = 1
            else:
                poblacion = 0
            nw = Cuadrante.crear_cuadrante(nivel - 1, poblacion)
            if self.matriz[f][c + 1] == "X":
                poblacion = 1
            else:
                poblacion = 0
            ne = Cuadrante.crear_cuadrante(nivel - 1, poblacion)
            if self.matriz[f + 1][c] == "X":
                poblacion = 1
            else:
                poblacion = 0
            sw = Cuadrante.crear_cuadrante(nivel - 1, poblacion)
            if self.matriz[f + 1][c + 1] == "X":
                poblacion = 1
            else:
                poblacion = 0
            se = Cuadrante.crear_cuadrante(nivel - 1, poblacion)
            return Cuadrante.crear_cuadrante(nivel, nw=nw, ne=ne, sw=sw, se=se)
        else:
            nw = self.cuadrante_raiz(nivel - 1, f=f, c=c)
            ne = self.cuadrante_raiz(nivel - 1, c=int((pow(2, nivel) / 2)) + c)
            sw = self.cuadrante_raiz(nivel - 1, f=int((pow(2, nivel) / 2)) + f)
            se = self.cuadrante_raiz(nivel - 1, c=int((pow(2, nivel) / 2) + c), f=int((pow(2, nivel) / 2)) + f)
            return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)

    def iteracion(self):
        """Genera una nueva iteracion del juego."""
        expandido = self.cuadrante.expandir()
        self.cuadrante = expandido.generacion()

    def imprimir(self):
        """Imprime por pantalla los resultados y guarda en un
        fichero la ultima iteración realizada."""
        print("{} iteraciones".format(self.iteraciones))
        print("{} celdas vivas".format(self.cuadrante.poblacion))
        print("Dimensiones {} x {}".format(pow(2, self.cuadrante.nivel), pow(2, self.cuadrante.nivel)))
        print("{:.2f} segundos".format(self.tiempo_final - self.tiempo_inicial))


if __name__ == "__main__":
    app = Aplicacion()
