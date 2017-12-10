#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan


class Par:
    """docstring for Par"""
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor


class TablaDispCer(object):
    """docstring for TablaDispCer"""
    def __init__(self, m=4, maxL=1):
        self.m = m
        self.n = 0
        self.maxL = maxL
        self.tabla = [None] * m

    def insertar(self, clave, cuadrante):
        print("--insertando--")
        self.n += 1
        if (float(self.n) / self.m) > self.maxL:
            self.reestructurar()

        i = self.indice(clave)
        s = self.salto(clave)
        while self.tabla[i] is not None and self.tabla[i].clave is not None:
            i = self.indice(i + s)
        if self.tabla[i] is None:
            self.tabla[i] = Par(clave, cuadrante)
        else:
            self.tabla[i].clave = clave
            self.tabla[i].valor = cuadrante

    def buscar(self, clave):
        print("--buscando--")
        i = self.indice(clave)
        s = self.salto(clave)
        while self.tabla[i] is not None and (self.tabla[i].clave is None or not self.tabla[i].clave == clave):
            i = self.indice(i + s)
        return None if self.tabla[i] is None else self.tabla[i].valor

    def salto(self, clave):
        s = clave / self.m
        if s < 0:
            s = -s
        if s % 2 == 0:
            s += 1
        return s

    def reestructurar(self):
        print("--reestructurando--")
        tabla_aux = self.tabla
        self.n = 0
        self.m = self.m * 2
        self.tabla = None * self.m
        for i in range(len(tabla_aux)):
            self.tabla = tabla_aux[i]
            if self.tabla is not None and self.tabla.clave is not None:
                self.insertar(self.tabla.clave, self.tabla.valor)

    def indice(self, clave):
        return int(clave % self.m)
