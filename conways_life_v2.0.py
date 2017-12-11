#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

from time import time
from cuadrante import Cuadrante
import sys

viva = "X"
muerta = "."


class Aplicacion():

    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.fichero = sys.argv[1]
        self.iteraciones = int(sys.argv[2])
        self.iteraciones_aprox = 0
        self.matriz = self.leer_fichero()
        self.tiempo_inicial = time()
        self.tiempo_final = 0
        self.main()

    def main(self):
        """Metodo main del programa."""
        cociente = len(self.matriz)
        nivel_raiz = 0
        while cociente != 1:
            cociente = cociente / 2
            nivel_raiz += 1
        self.cuadrante = self.cuadrante_raiz(nivel_raiz)

        for x in range(self.iteraciones):
            self.iteracion()
            if self.iteraciones_aprox >= self.iteraciones:
                break
        self.tiempo_final = time()

        # Matriz auxiliar para guardar los valores resultantes de la ultima iteracion realizada
        self.matriz_aux = [([""] * (pow(2, self.cuadrante.nivel))) for i in range(pow(2, self.cuadrante.nivel))]
        self.valores(self.cuadrante)
        for line in self.matriz_aux:
            print(line)
        self.limites()
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

            matriz_aux = [([muerta] * c) for i in range(c)]
            for n in range(filas):
                for m in range(columnas):
                    matriz_aux[n][m] = matriz[n][m]

        return matriz_aux

    def cuadrante_raiz(self, nivel, f=0, c=0):
        """Crea el cuadrante raiz de la matriz leida en el fichero."""
        if nivel == 0:
            if self.matriz[f][c] == viva:
                poblacion = 1
            else:
                poblacion = 0

            return Cuadrante.crear_cuadrante(nivel, poblacion)
        else:
            nw = self.cuadrante_raiz(nivel - 1, f=f, c=c)
            ne = self.cuadrante_raiz(nivel - 1, c=int((pow(2, nivel) / 2)) + c)
            sw = self.cuadrante_raiz(nivel - 1, f=int((pow(2, nivel) / 2)) + f)
            se = self.cuadrante_raiz(nivel - 1, c=int((pow(2, nivel) / 2) + c), f=int((pow(2, nivel) / 2)) + f)
            return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)

    def iteracion(self):
        """Genera 2^(n-2) iteraciones como marca la etapa 4 de la practica."""
        self.cuadrante = self.cuadrante.expandir()
        self.iteraciones_aprox += pow(2, (self.cuadrante.nivel - 2))
        self.cuadrante = self.cuadrante.generacion()

    def imprimir(self):
        """Imprime por pantalla los resultados y guarda en un fichero los valores
        de la ultima iteración realizada."""
        print("{} iteraciones".format(self.iteraciones))
        print("{} iteraciones calculadas".format(self.iteraciones_aprox))
        print("{} celdas vivas".format(self.cuadrante.poblacion))
        print("Dimensiones {} x {}".format(len(self.matriz_aux), len(self.matriz_aux[0])))
        print("{:.2f} segundos".format(self.tiempo_final - self.tiempo_inicial))
        self.fichero_salida()

    def valores(self, arbol, f=0, c=0):
        """Transforma la poblacion de los nodos de nivel 0 en vivas("X") o muertas(".").
        Lo almacena en una matriz, segun la posicion del nodo dentro del arbol."""
        if arbol.nivel == 0:
            if arbol.poblacion == 1:
                valor = viva
            else:
                valor = muerta
            self.matriz_aux[f][c] = valor
            return 1
        else:
            self.valores(arbol.nw, f=f, c=c)
            self.valores(arbol.ne, f=f, c=c + int((pow(2, arbol.nivel) / 2)))
            self.valores(arbol.sw, f=f + int((pow(2, arbol.nivel) / 2)), c=c)
            self.valores(arbol.se, f=f + int((pow(2, arbol.nivel) / 2)), c=c + int((pow(2, arbol.nivel) / 2)))
            return 1

    def limites(self):
        """Elimina de la matriz las filas y columnas con todas las celdas muertas."""
        filas = len(self.matriz_aux)
        columnas = len(self.matriz_aux)

        flimites = [False] * filas
        climites = [False] * columnas
        for n in range(filas):
            for m in range(columnas):
                if self.matriz_aux[n][m] == viva:
                    flimites[n] = True
                    break
        for m in range(columnas):
            for n in range(filas):
                if self.matriz_aux[n][m] == viva:
                    climites[m] = True
                    break

        if flimites.index(True) == 0:
            pass
        elif flimites.index(True) > 0:
            for x in range(flimites.index(True)):
                filas -= 1
                self.matriz_aux.pop(0)
        if flimites[::-1].index(True) == 0:
            pass
        elif flimites[::-1].index(True) > 0:
            for x in range(flimites[::-1].index(True)):
                self.matriz_aux.pop(filas - 1)
                filas -= 1

        if climites.index(True) == 0:
            pass
        elif climites.index(True) > 0:
            for x in range(climites.index(True)):
                columnas -= 1
                for fila in self.matriz_aux:
                    fila.pop(0)
        if climites[::-1].index(True) == 0:
            pass
        elif climites[::-1].index(True) > 0:
            for x in range(climites[::-1].index(True)):
                for fila in self.matriz_aux:
                    fila.pop(columnas - 1)
                columnas -= 1

    def fichero_salida(self):
        """Guarda la última iteración en el fichero"""
        nombre = input("Escriba el nombre del fichero de salida: ")
        try:
            fichero = open(nombre, "w")
        except OSError:
            sys.exit("Algo salio mal al guardar '{}'".format(nombre))
        else:
            fichero.write(str(len(self.matriz_aux)) + "\n")
            fichero.write(str(len(self.matriz_aux[0])))
            for n in range(len(self.matriz_aux)):
                fichero.write("\n")
                for m in range(len(self.matriz_aux[0])):
                    fichero.write(self.matriz_aux[n][m])
            fichero.close()


if __name__ == "__main__":
    app = Aplicacion()
