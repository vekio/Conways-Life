#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

from time import time
from cuadrante import Cuadrante
import sys

viva = "X"

class Aplicacion():

    """Clase Aplicacion del juego Conway's Life"""
    def __init__(self):
        self.fichero = sys.argv[1]
        self.iteraciones = int(sys.argv[2])
        self.matriz = self.leer_fichero()
        self.matriz_aux = list()

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
            # print("--iteracion ", x)
            self.iteracion()
        # for line in self.matriz_aux:
        #    print(line)
        self.tiempo_final = time()
        self.limites()
        for line in self.matriz_aux:
            print(line)
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
        # expandido = self.cuadrante.expandir()
        # print(expandido.nivel)
        # print(expandido.poblacion)
        self.cuadrante = self.cuadrante.expandir().generacion()
        self.matriz_aux = [([""] * (pow(2, self.cuadrante.nivel))) for i in range(pow(2, self.cuadrante.nivel))]
        self.valores(self.cuadrante)
        #for line in self.matriz_aux:
        #    print(line)

    def imprimir(self):
        """Imprime por pantalla los resultados y guarda en un
        fichero la ultima iteración realizada."""
        print("{} iteraciones".format(self.iteraciones))
        print("{} celdas vivas".format(self.cuadrante.poblacion))
        print("Dimensiones {} x {}".format(pow(2, self.cuadrante.nivel), pow(2, self.cuadrante.nivel)))
        print("{:.2f} segundos".format(self.tiempo_final - self.tiempo_inicial))
        self.fichero_salida()

    def valores(self, arbol, f=0, c=0):
        """Imprime los valores por pantalla"""
        if arbol.nivel == 0:
            if arbol.poblacion == 1:
                valor = "X"
            else:
                valor = "."
            self.matriz_aux[f][c] = valor
            return 1
        else:
            self.valores(arbol.nw, f=f, c=c)
            self.valores(arbol.ne, f=f, c=c + int((pow(2, arbol.nivel) / 2)))
            self.valores(arbol.sw, f=f + int((pow(2, arbol.nivel) / 2)), c=c)
            self.valores(arbol.se, f=f + int((pow(2, arbol.nivel) / 2)), c=c + int((pow(2, arbol.nivel) / 2)))
            return 1

    def limites(self):
        """Comprueba filas y columnas con celdas vivas
        y añade/elimina filas/columnas."""
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
            for x in range(flimites.index(True) - 2):
                filas -= 1
                self.matriz_aux.pop(0)
        if flimites[::-1].index(True) == 2:
            pass
        elif flimites[::-1].index(True) < 2:
            for x in range(2 - flimites[::-1].index(True)):
                self.matriz_aux.insert(filas, ["."] * columnas)
                filas += 1
        elif flimites[::-1].index(True) > 2:
            for x in range(flimites[::-1].index(True) - 2):
                self.matriz_aux.pop(filas - 1)
                filas -= 1

        if climites.index(True) == 2:
            pass
        elif climites.index(True) < 2:
            for x in range(2 - climites.index(True)):
                columnas += 1
                for fila in self.matriz_aux:
                    fila.insert(0, ".")
        elif climites.index(True) > 2:
            for x in range(climites.index(True) - 2):
                columnas -= 1
                for fila in self.matriz_aux:
                    fila.pop(0)
        if climites[::-1].index(True) == 2:
            pass
        elif climites[::-1].index(True) < 2:
            for x in range(2 - climites[::-1].index(True)):
                for fila in self.matriz_aux:
                    fila.insert(columnas, ".")
                columnas += 1
        elif climites[::-1].index(True) > 2:
            for x in range(climites[::-1].index(True) - 2):
                for fila in self.matriz_aux:
                    fila.pop(columnas - 1)
                columnas -= 1

    def fichero_salida(self):
        """Escribe la ultima iteración en el fichero dado por el usuario"""
        nombre = input("Escriba el nombre del fichero de salida: ")
        try:
            fichero = open(nombre, "w")
        except OSError:
            sys.exit("Algo salio mal al guardar '{}'".format(nombre))
        else:
            fichero.write(str(len(self.matriz_aux) - 2) + "\n")
            fichero.write(str(len(self.matriz_aux) - 2))
            for n in range(2, len(self.matriz_aux) - 2):
                fichero.write("\n")
                for m in range(2, len(self.matriz_aux) - 2):
                    fichero.write(self.matriz_aux[n][m])
            fichero.close()


if __name__ == "__main__":
    app = Aplicacion()
