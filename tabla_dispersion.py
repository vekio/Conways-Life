#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan


class Par:
    """Clase Par que almacena pares de atributos(clave, valor)."""
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor


class TablaDispCer(object):
    """Clase TablaDispCer que crea una TAD cerrada."""
    def __init__(self, m=4, maxL=1.0):
        self.m = m
        self.n = 0
        self.maxL = maxL
        self.tabla = [None] * m

    def insertar(self, clave, cuadrante):
        """Metodo para insertar un cuadrante en la tabla de dispersion dada su clave."""
        self.n += 1
        if (float(self.n) / self.m) >= self.maxL:
            self.reestructurar()
        i = self.indice(clave)
        s = self.salto(clave)
        while True:
            if self.tabla[i] is None:
                break
            else:
                i = (i + s) % self.m
        if self.tabla[i] is None:
            self.tabla[i] = Par(clave, cuadrante)

    def buscar(self, clave):
        """Metodo que busca un cuadrante en la tabla de dispersion dando una clave conocida.
        Devuelve el cuadrante si lo encuentra o None si no esta dentro."""
        i = self.indice(clave)
        s = self.salto(clave)
        while True:
            if self.tabla[i] is None:
                break
            else:
                if self.tabla[i].clave == clave:
                    break
                else:
                    i = (i + s) % self.m
        if self.tabla[i] is None:
            return None
        else:
            return self.tabla[i].valor

    def salto(self, h):
        """Calcula el salto para recorrer la tabla de dispersion."""
        h = h ^ (h >> 20) ^ (h >> 12)
        h = h ^ (h >> 7) ^ (h >> 4)
        s = h / self.m
        s = int(s)
        if s < 0:
            s = -s
        if s % 2 == 0:
            s += 1
        return s

    def indice(self, h):
        """Calcula el indice inicial para recorrer la tabla de dispersion."""
        h = h ^ (h >> 20) ^ (h >> 12)
        h = h ^ (h >> 7) ^ (h >> 4)
        return int(h % self.m)

    def reestructurar(self):
        """Duplica el tamaño de la tabla."""
        tabla_aux = self.tabla
        self.n = 1
        self.m = self.m * 2
        self.tabla = [None] * self.m
        for i in range(len(tabla_aux)):
            w = tabla_aux[i]
            if w is not None:
                self.insertar(w.clave, w.valor)
