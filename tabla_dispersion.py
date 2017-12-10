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
    def __init__(self, m, maxL=1.0):
        self.m = m
        self.n = 0
        self.maxL = maxL
        self.tabla = [None] * m

    def insertar(self, clave, cuadrante):
        # print("--insertando--")
        self.n += 1
        # print(self.tabla)
        if (float(self.n) / self.m) >= self.maxL:
            self.reestructurar()
        # print(self.n)

        i = self.indice(clave)
        s = self.salto(clave)

        """print(self.tabla[i].clave is not None)
        print(self.tabla[i] is not None)"""
        while True:
            if self.tabla[i] is None:
                break
            else:
                i = (i + s) % self.m
        if self.tabla[i] is None:
            # print("inserto en ", i)
            self.tabla[i] = Par(clave, cuadrante)
        """else:
            self.tabla[i].clave = clave
            self.tabla[i].valor = cuadrante"""
        # print(self.tabla)

    def buscar(self, clave):
        # print("--buscando--")
        # print(clave)
        i = self.indice(clave)
        s = self.salto(clave)
        # print("primera posicion de buscar ", i)
        # print(s)
        while True:
            if self.tabla[i] is None:
                break
            else:
                if self.tabla[i].clave == clave:
                    break
                else:
                    i = (i + s) % self.m
                    # print("buscando en ", i)

        """
        while self.tabla[i] is not None and (self.tabla[i].clave == clave):
            print("busco en ", i)
            i = self.indice(i + s)
        """
        # print("--buscando2--")
        if self.tabla[i] is None:
            return None
        else:
            return self.tabla[i].valor

    def salto(self, h):
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
        h = h ^ (h >> 20) ^ (h >> 12)
        h = h ^ (h >> 7) ^ (h >> 4)
        return int(h % self.m)

    def reestructurar(self):
        # print("--reestructurando--")
        tabla_aux = self.tabla
        self.n = 1
        self.m = self.m * 2
        self.tabla = [None] * self.m
        for i in range(len(tabla_aux)):
            w = tabla_aux[i]
            if w is not None:
                self.insertar(w.clave, w.valor)
        # print(self.tabla)
